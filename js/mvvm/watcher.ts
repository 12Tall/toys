/// <reference path="observer.ts" />
namespace Watcher {
    // 回调函数类型
    // 因为计算属性需要根据其他属性计算得到最终值，所以返回值设置为any
    type CallBack = () => any;
    var _watcher: Observer.IListener | null = null;

    /**
     * 给对象设置计算属性
     * @param obj 目标对象
     * @param prop 属性名，一般是新增属性
     * @param cb 回调函数，在获取属性时调用
     */
    function defineComputed(obj: Observer.IObserverable, prop: string, cb: CallBack) {
        // 因为每个变量只会初始化一次，所以不会重复
        // 前提：configurable: false
        const watcher: Observer.IListener = {
            update() {
                console.log("计算属性更新了！");
                // const val = cb();
            }
        }

        Object.defineProperty(obj, prop, {
            enumerable: true,
            configurable: true,
            get() {
                // 在这里，需要将cb 添加到publisher 的监测者里面
                // 其实应该按属性分类监听的
                _watcher = watcher;
                const val = cb();
                _watcher = null;
                // 通知下一级
                return val;
            },
            set() {
                console.error("不可赋值给计算属性！");
            }
        });
    }

    // 2. 如果属性D是通过其他属性S计算后得到的，那么属性S 变化也要通知到属性D
    /**
     * 想象下调用顺序：
     * 1. 访问计算属性的get 才会生效
     * 2. 如果计算属性中引用了其他属性，就一定会访问其他属性的get 方法，这点很重要！！！
     * 3. 所以我们可以在其他属性的get 方法中添加计算属性作为监听器
     * 
     * 存在问题：
     * 1. 计算属性中的监听器无法与普通属性互通
     *    所以需要一个全局变量暂存Watcher 对象
     * 2. 如果考虑多线程的话，全局变量就可能会有冲突
     *  */

    function defineReactive(obj: Observer.IObserverable, prop: string, val: any) {
        Object.defineProperty(obj, prop, {
            enumerable: true,
            configurable: true,
            get() {
                // 为什么会有死循环呢？
                // listeners 也被设置了get
                if (obj.listeners.indexOf(_watcher) === -1) {
                    obj.addListener(_watcher);
                }
                return val;
            },
            set(newVal: any) { // 如果值被改变，则让对象发布更新
                if (newVal !== val) {
                    val = newVal;
                    obj.notify();
                }
            }

        })
    }

    function Observer(obj: Observer.IObserverable): void {
        if (obj && typeof obj === 'object') {
            // Object.keys 会列出所有属性，包含函数
            Object.keys(obj).forEach((prop: string) => {
                // 这里会造成死循环！
                // 所以可以采用闭包的方法解决
                // 而不是listeners
                if (prop !== 'listeners' && prop !== 'addListener' && prop !== 'notify') {
                    defineReactive(obj, prop, obj[prop]);
                }
            })
        }
    }

    // 1. 在属性被读取(`get()`) 时，才转化为可观测的  
    // 注意是var 而不是class，因为js 本身没有类这个概念吧
    // 定义监听器
    var listener: Observer.IListener = {
        update: (result: string): void => {
            console.log(result);
        }
    }

    // 定义发布者
    var publisher: Observer.IObserverable = {
        name: "12tall",
        listeners: new Array<Observer.IListener>(),
        addListener: (listener: Observer.IListener) => {
            console.log(publisher.listeners)
            publisher.listeners.push(listener);
        },
        notify: () => {
            publisher.listeners.forEach(listener => {
                listener.update(`name updated:${publisher.name}`);
            });
        }
    }

    // 发布者添加监听器
    // publisher.addListener(listener);

    Observer(publisher);
    // defineReactive(publisher,"name","12tall");

    // 将某个属性变为可观测对象
    defineComputed(publisher, "age", () => {
        console.log("访问了计算属性");
        return publisher.name + ": 12 years old!";
    });
    console.log(publisher.age);
    publisher.name = "12 and tall";


    // publisher.age = "12 and tall";
}