// 参考自知乎专栏：https://zhuanlan.zhihu.com/p/29318017

/**
 * 依赖收集器
 * */
class Dep {
    constructor() {
        this.target = null;
    }
}

// 新建一个全局依赖收集器
var dep = new Dep();


/**
 * 将一个对象转化为可观测的对象
 * @param {Object} obj 目标对象
 * @param {String} prop 属性名
 * @param {Any} val 值
 * */
function defineReactive(obj, prop, val) {
    const deps = [];
    Object.defineProperty(obj, prop, {
        get() {
            /**
             * 8. 获取属性，并将watcher 订阅者的方法，绑定到deps
             * */
            console.log(`${obj}的${prop}属性被读取：${val}`);
            if (dep.target && deps.indexOf(dep.target) === -1) {
                // 如果没有绑定监听器，则绑定
                // 为什么在get 里面绑定就可以了？
                // ⚠ 因为在计算属性中的回调函数如果用到此属性的话，就一定会用到get 方法
                deps.push(dep.target);
            }
            return val;
        },
        set(newVal) {
            console.log(`${obj}的${prop}属性被修改：${newVal}`);
            val = newVal;
            /**
             * 10. 修改时发出通知
             * */
            deps.forEach(dep => {
                dep();
            });
        }
    });
}

/**
 * 将一个对象的所有属性都转化为可观测对象
 * @param {Object} obj 目标对象
 * */
function observer(obj) {
    if (!obj || typeof obj !== 'object') {
        return obj;
    }
    Object.keys(obj).forEach(prop => {
        defineReactive(obj, prop, obj[prop]);
    })
    return obj;
}

// 可观测的意思就是，该属性的值改变之后，会自动通知订阅者(依赖项)
// 依赖收集器，可能只是一个中间缓存

/**
 * 当计算属性被更新时调用
 * @param {Any} val 值
 * */
function onComputedUpdate(val) {
    console.log(`计算属性被更新${val}`);
}

/**
 * 观测者(订阅者)：监听对象的某个属性
 * @param {Object} obj 目标对象
 * @param {String} key 属性(prop)，一般是不存在的属性
 * @param {function} cb 回调函数
 * */
function watcher(obj, key, cb) {
    /**
     * 2. 定义一个被动触发函数
     * 当被观测对象更新时调用
     * */
    const onDepUpdate = () => {
        const val = cb();
        onComputedUpdate(val);
    }

    /**
     * 3. 设置get/set 方法
     * */
    Object.defineProperty(obj, key, {
        /**
         * 5. 在获取属性值的时候，会调用get 方法
         * */
        get() {
            // 设置target，回调函数会用到
            dep.target = onDepUpdate;
            /**
             * 6. 调用回调函数
             * */
            const val = cb();
            // 用完之后重置
            dep.target = null;
            return val;
        },
        set(newVal) {
            console.error("无法赋值给计算属性！")
        }
    })
}

const hero = observer({
    health: 3000,
    IQ: 150
})

/**
 * 1. 设置计算属性hero.type
 * */
watcher(hero, 'type', () => {
    /**
     * 7. 读取hero.health 会触发get 方法
     * */
    return hero.health > 4000 ? '坦克' : '脆皮';
});

/**
 * 4. 必须要读取一次初始化才行
 * */
console.log(hero.type);
/**
 * 9. 改变值
 * */
hero.health = 5000;
hero.IQ = 5000;
