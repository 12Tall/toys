namespace Observer {
    // 接口的属性是固定的！

    // 导出监听者接口
    export interface IListener {
        // 接收通知，更新
        update(result: string): void;
    }

    // 导出被监听者接口
    export interface IObserverable {
        // 属性
        name: string;
        age?: any;
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
    export function defineReactive(obj: IObserverable, prop: string, val: any): void {
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

    /**
    * 将一个对象的所有属性转化为可观测的
    * @param {IObserverable} obj 目标对象
    */
    export function Observer(obj: IObserverable): void {
        if (obj && typeof obj === 'object') {
            Object.keys(obj).forEach((prop: string) => {
                defineReactive(obj, prop, obj[prop]);
            })
        }
    }

}