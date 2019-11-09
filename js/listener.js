/**
 * 将对象的属性定义为可观测的
 * @param obj 对象
 * @param prop 属性
 * @param val 值
 * @summary 其实这里还可以再传入一个回调函数，或者
 * 给notify() 传入一个值，用于可能会用到的自定义操作
 */
function defineReactive(obj, prop, val) {
    Object.defineProperty(obj, prop, {
        enumerable: true,
        configurable: true,
        get: function () {
            return val;
        },
        set: function (newVal) {
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
var listener = {
    update: function (result) {
        console.log(result);
    }
};
// 定义发布者
var publisher = {
    name: "12tall",
    listeners: new Array(),
    addListener: function (listener) {
        publisher.listeners.push(listener);
    },
    notify: function () {
        publisher.listeners.forEach(function (listener) {
            listener.update("name updated:" + publisher.name);
        });
    }
};
// 发布者添加监听器
publisher.addListener(listener);
// 将某个属性变为可观测对象
// defineReactive(publisher, "name", "12tall");
// publisher.name = "12 and tall";
/**
 * 将一个对象的所有属性转化为可观测的
 * @param {IObserverable} obj 目标对象
 */
function Observer(obj) {
    if (obj && typeof obj === 'object') {
        Object.keys(obj).forEach(function (prop) {
            defineReactive(obj, prop, obj[prop]);
        });
    }
}
// Observer(publisher);
publisher.name = "12 and tall";
