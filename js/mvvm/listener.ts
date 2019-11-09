/// <reference path="observer.ts"/>
namespace Listener1 {
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


    Observer.Observer(publisher);
    publisher.name = "12 and tall";

}
