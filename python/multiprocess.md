# 多进程_笔记  

## fork()函数  

`fork()`，复刻。可以将运行的进程`从当前位置` 创建一个几乎一样的副本(主要是执行环境一样，并非共享执行环境，但也并不是重新创建)，父进程已经执行的代码在子进程中是不会执行的。[CSDN](https://blog.csdn.net/xiang_shao344/article/details/83026932)中表述的比较清晰。在调用`fork()` 时，若调用成功，父进程中返回子进程的`pid`，子进程返回`0`(成功) 或`-1`(失败)。  

## fork_in_python  

```python
import os
print("main pid is %s"%os.getpid())
# os.fork() 只有在*nix 系统中可用
pid = os.fork()
# 因为子进程并未执行os.fork() 所以pid = 0
if pid == 0:
    print("this is child, pid is %s and parentId is %s" % (os.getpid(),os.getppid()))
else:
    print("this is main")
```

## multiprocessing  

跨平台的多进程库  

```python
from multiprocessing import Process
import os

def fun(param):
    print("child pid is %s,get param %s",(os.getpid(),param))

if __name__ == "__main__":
    print("main pid is %s"%os.getpid())
    p = Process(target=fun,args=("test",))
    # 这种调用方法更像是直接调用函数。。。
    print("child start...")
    p.start()
    # 等子进程执行完毕后才会继续执行
    p.join()
    print("child end")
```

`multiprocessing` 自带了进程池`Pool` 可以批量创建子进程：

```python
from multiprocessing import Pool
# 这个池大小一般默认是cpu 核数
p = Pool(4)
for i in range(5):
    p.apply_async(fun, args=(i,))
print('Waiting for all subprocesses done...')
# close() 之后不能再添加新的进程
p.close()
# join() 之前必须先close()
p.join()
```

## subprocess_子进程  

可以方便地控制进程的输入和输出  

```python
# 调用nslookup www.python.org 查询url
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
```

```python
# 调用nslookup 传入命令
import subprocess

print('$ nslookup')
# 重定位输入输出到subprocess.PIPE
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 输入命令
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# set q=mx
# python.org
# exit
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
```

## 进程间通信  

- 管道`pipe`：半双工，数据只能单向流动，只能在父子进程中使用。使用时一般需要建立两个管道；  
- 命名管道`FIFO`：半双工，可以在无亲缘关系的进程间通信；  
- 消息队列`MessageQueue`：  
- 共享存储`SharedMemory`：最快的方式；  
- 信号量`Semaphore`：一个计数器，用于控制多个进程对共享资源的的访问，一般用作线程间的同步手段；  
- 套接字`Socket`：；
- 信号`signal`：。

```python
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':

    # 父进程创建Queue，并传给各个子进程：
    q = Queue()

    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```