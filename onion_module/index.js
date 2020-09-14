var fns = [
    (next) => { console.log(`1 in`); next(); console.log(`1 out`) },
    (next) => { console.log(`2 in`); next(); console.log(`2 out`) },
    (next) => { console.log(`3 in`); next(); console.log(`3 out`) },
    (next) => { console.log(`4 in`); next(); console.log(`4 out`) },
    (next) => { console.log(`5 in`); /* next(); */ console.log(`5 out`) },  // 中断了传递
    (next) => { console.log(`6 in`); next(); console.log(`6 out`) },
]

// 1. 手动
// 将后面的函数，重新封装
let param = 0;
fns[0](() => {
    fns[1](() => {
        console.log(`over`)
    });
});
console.log(`=============================`)
// 2. 递归

var i = 0;
function dispatch(i) {
    if (i === fns.length) {
        return;
    }
    // 最后会返回一个空函数
    return fns[i](() => { dispatch(i + 1) });
}

dispatch(0);

console.log(`=============================`)

// 3. 递归传参  
var fns_2 = [
    (para, next) => { var i = ++para.value; console.log(`${i} in`); next(); console.log(`${i} out`) },
    (para, next) => { var i = ++para.value; console.log(`${i} in`); next(); console.log(`${i} out`) },
    (para, next) => { var i = ++para.value; console.log(`${i} in`); next(); console.log(`${i} out`) },
    (para, next) => { var i = ++para.value; console.log(`${i} in`); next(); console.log(`${i} out`) },
    (para, next) => { var i = ++para.value; console.log(`${i} in`); /* next(); */ console.log(`${i} out`) },
    (para, next) => { var i = ++para.value; console.log(`${i} in`); next(); console.log(`${i} out`) },
]

var para = { value: 0 };
/**
 * 1. 写法简单
 * 2. 
 */
function dispatch2(i) {
    if (i === fns_2.length) {
        return;
    }
    fns_2[i](para, () => { dispatch2(i + 1) });
}

dispatch2(0);