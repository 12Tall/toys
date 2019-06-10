# 关于JavaScript  

## 原型(proto)  

### 对象、构造器与原型  

- 对象不存在原型，对象的原型实际上是指构造器的原型  

> 浏览器中，对象有`__proto__` 指向构造器的原型`Constructor.prototype`  

- 构造器才有原型  

> 构造器的原型由构造器的`prototype` 指定  

- 构造器是函数  
- 构造器的原型是对象  
- 最根本的原型：`Object.prototype`  

> 可见，`Object` 本身也是一个函数  

### 创建对象  

- `new Construcor()` 效率最高  
- `Object.create(protoObject)` 以`protoObject` 对象为原型创建对象  
- `Object.create(null)` 创建没有原型的对象  

## 执行环境(this)

之所以这样写，是因为this 实在是太像执行环境(`context`)了。`this` 对象存在于函数中，对于`this` 的指向，一般有以下规律  

### 谁开发谁保护：  

- 对象调用自身的方法，`this` 指向对象本身。  

```javascript
var obj = {
    name:"12tall",
    sayHi:function(){
        console.log("hi! I'am " + this.name);
    }
}
obj.sayHi();  // hi! I'am 12tall
```

- 直接调用，`this` 指向最外层执行环境。浏览器中是`window`，严格模式下是`undefined`  

```javascript
var name = "12tall";
var sayHi = function(){
    console.log("hi! I'am " + this.name);
};
sayHi();  // hi! I'am 12tall
```  

> 对象的方法如果被`直接调用`，`this` 也是指向最外层执行环境。  

```javascript
// 注意不能是严格模式  
var name = "tall12";
var obj = {
    name:"12tall",
    sayHi:function(){
        console.log("hi! I'am " + this.name);
    }
}
var sayHi = obj.sayHi;
sayHi();  // hi! I'am tall12
```

- `构造器` 比较特殊，通过`new` 运算符调用，`this` 一般指向生成的对象并且返回`this`(除非显式声明不返回`this`)  

- `call(obj,...)`,`apply(obj,[])` 可以人为指定执行环境。第一个参数是`运行环境`  

> `call` 是`apply` 的语法糖  
> `call` 效率低一些  
> `call` 是可变参数，`apply` 第二个参数是一个数组。二者几乎没什么区别  

- 关于`回调函数`，无论什么样的函数、在哪里调用，都可以参考以上分类  
