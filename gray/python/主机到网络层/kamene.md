# kamene  

## 简单示例  

```python
# python3 中scapy 变成了kamene

import sys
import time

import logging

# 隐藏警告
# WARNING: No route found for IPv6 destination :: (no default route?). This affects only IPv6
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


# 需要安装winpcap 否则会报错
# WindowsError: [Error 126]
# _lib=CDLL('wpcap.dll')

from kamene.all import *

# getmacbyip 虽然不会在pycharm 中提示，但是可以用
# 通过下面命令可以找到所有属性
# print(dir(kamene.all))
mac = getmacbyip("192.168.1.1")
print(mac)
```