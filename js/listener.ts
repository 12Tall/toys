/********** 定义接口 ************/
/**
 * 监听者接口
 */
interface IListener {
    // 接收通知，更新
    update(result: string): void;
}

/**
 * 被监测者接口
 */
interface IObserverable {
    // 属性
    name: string;
    // 监听器，因为可能不止一个，所以采用数组
    listeners: Array<IListener>;
    // 添加监听器
    addListener(listener: IListener): void;
    // 发布更新
    notify(): void;
}

/**
 * 将对象的属性定义为可观测的
 * @param obj 对象
 * @param prop 属性
 * @param val 值
 * @summary 其实这里还可以再传入一个回调函数，或者
 * 给notify() 传入一个值，用于可能会用到的自定义操作
 */
function defineReactive(obj: IObserverable, prop: string, val: any): void {
    Object.defineProperty(obj, prop, {
        enumerable: true,   // 该属性可以被枚举
        configurable: true, // 该属性的修饰符可以被修改
        get() {
            return val;
        },
        set(newVal) {
            // 如果值被改变，则让对象发布更新
            if (newVal !== val) {
                val = newVal;
                obj.notify();
            }
        }
    });

    return;
}

/************** 接口的实现 ****************/

// 注意是var 而不是class，因为js 本身没有类这个概念吧
// 定义监听器
var listener: IListener = {
    update: (result: string): void => {
        console.log(result);
    }
}

// 定义发布者
var publisher: IObserverable = {
    name: "12tall",
    listeners: new Array<IListener>(),
    addListener: (listener: IListener) => {
        publisher.listeners.push(listener);
    },
    notify: () => {
        publisher.listeners.forEach(listener => {
            listener.update(`name updated:${publisher.name}`);
        });
    }
}

// 发布者添加监听器
publisher.addListener(listener);

// 将某个属性变为可观测对象
// defineReactive(publisher, "name", "12tall");
// publisher.name = "12 and tall";

/**
 * 将一个对象的所有属性转化为可观测的
 * @param {IObserverable} obj 目标对象
 */
function Observer(obj: IObserverable): void {
    if (obj && typeof obj === 'object') {
        Object.keys(obj).forEach((prop: string) => {
            defineReactive(obj, prop, obj[prop]);
        })
    }
}

Observer(publisher);
publisher.name = "12 and tall";