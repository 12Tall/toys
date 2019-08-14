# 阮一峰《webpack-demos.md》 的翻译  

本仓库由一系列`webpack` 的简单demo 组成。  
这些demo 专门为学习目的而写，具有简单、清晰的风格。跟随这些demo 可以轻松的入门`webpack`这个强大的工具。  

## 如何使用本仓库  

首先，全局安装[webpack](https://www.npmjs.com/package/webpack) 和[webpack-dev-server](https://www.npmjs.com/package/webpack-dev-server)。*译注：本文假设你已经安装了`nodejs`*  

```bash
#
$ npm i -g webpack webpack-dev-server
```  

然后克隆[本仓库](https://github.com/ruanyf/webpack-demos)。

```bash
#
$ git clone https://github.com/ruanyf/webpack-demos.git
```  

安装依赖。

```bash
#
$ cd webpack-demos
$ npm install
```

准备工作完成之后，在相应的`demo*` 目录下，利用源文件就可以运行了

```bash
#
$ cd demo01
$ npm run dev
```

如果以上命令没能自动打开你的浏览器，那么你可能需要手动访问<http://127.0.0.1:8080> 了。  

> 译注：  
> 在本地创建目录的话，上面的命令还不够，下面的命令会帮助创建一个可以运行的新项目  
>  
> ```bash
>
> # 仅供参考
> $ npm i -g webpack webpack-dev-server webpack-cli
> $ mkdir demo
> $ cd demo
> $ npm init
> $ # 这里需要进行一堆配置，不熟悉默认就行
> $ npm i webpack webpack-dev-server webpack-cli --dev-save
> $ # 如果执行上面的命令的话，就不好用。。。。。。。。。
> $ npm install
> ```  

## 前言：什么是Webpack  

`webpack` 是一个面向浏览器的前端`Javascript` 构建工具。  
用法和`Browserify` 类似，但功能要更强大。  

```bash
#
$ browserify main.js > bundle.js
$ # 等同于
$ webpack main.js bundle.js
```

`webpack` 的配置文件是一个`CommonJS` 模块，叫做`webpack.config.js`。  

```js
// webpack.config.js
module.exports = {
    entry: './main.js',
    output: {
        filename: 'bundle.js'
    }
}
```

建立了`webpack.config.js` 后，就可以直接调用`webpack`。  

```bash
#
$ webpack
```  

下面是一些常用的参数选项：  

- `webpack` - 构建部署用文件  
- `webpack -p` - 构建生产用文件(压缩的)  
- `webpack --watch` - 用于连续增量构建(热更新？)  
- `webpack -d` - 包含源映射(source map)  
- `webpack --colors` - 美化构建输出  

我们可以自定义`package.json` 文件的`scripts` 字段保存常用命令。  

```js
// package.json
{
    // ...
    "scripts": {
        "dev": "webpack-dev-server --devtool eval --progress --colors",
        "deploy": "NODE_ENV=production webpack -p"
    },
    // ...
}
```  

## 目录  

1. [入口文件](#入口文件-源码)  
2. [多个入口文件](#多个入口文件-源码)  
3. [Babel 加载器](#Babel-加载器-源码)  
4. [CSS 加载器](#CSS-加载器-源码)  
5. [图片加载器](#图片加载器-源码)  
6. [CSS 模块](#CSS-模块-源码)  
7. [UglifyJs 插件](#UglifyJs-插件-源码)  
8. [HTML 插件与OpenBrowser 插件](#HTML-插件与OpenBrowser-插件-源码)  
9. [环境标识](#环境标识-源码)  
10. [代码拆分](#代码拆分-源码)  
11. [利用Babel 加载器进行代码拆分](#利用Babel-加载器进行代码拆分-源码)  
12. [公共代码块](#公共代码块-源码)  
13. [自有代码块](#自有代码块-源码)  
14. [全局公开变量](#全局公开变量-源码)  
15. [React 路由](#React-路由-源码)  

## 入口文件 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo01))  

入口文件(`Entry File`)是由`webpack` 读取，用来生成目标文件(如：`bundle.js`)  
假设`main.js` 是一个入口文件。  

```js
// main.js
document.write('<h1>Hello World</h1>');
```

index.html  

```html
<html>
  <body>
    <script type="text/javascript" src="bundle.js"></script>
  </body>
</html>
```

而`webpack` 会根据`webpack.config.js` 来构建`bundle.js`  

```js
// webpack.config.js
module.exports = {
  entry: './main.js',
  output: {
    filename: 'bundle.js'
  }
};
```

启动服务，并访问<http://127.0.0.1:8080/>。  

```bash
#
$ cd demo01
$ npm run dev
```

## 多个入口文件 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo02))  

`webpack` 允许同时构建多个文件。对于创建多页应用这一点非常有用。  

```js
// main1.js
document.write('<h1>Hello World</h1>');

// main2.js
document.write('<h2>Hello Webpack</h2>');
```

index.html

```html
<html>
  <body>
    <script src="bundle1.js"></script>
    <script src="bundle2.js"></script>
  </body>
</html>
```

`webpack.config.js`  

```js
module.exports = {
  entry: {
    bundle1: './main1.js',
    bundle2: './main2.js'
  },
  output: {
    // 注意方括号里面的内容
    filename: '[name].js'
  }
};
```

## Babel 加载器 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo03))  

[加载器](https://webpack.js.org/concepts/loaders/)可以将源文件在`webpack` 构建之前进行预处理。  
例如：[Babel 加载器](https://www.npmjs.com/package/babel-loader) 可以将`JSX/ES6` 的代码转换成正常JS 文件(*译注：一般是指ES2015*)，然后再由`webpack` 进行构建工作。`webpack`官方文档包含有一份完整的[加载器列表](https://webpack.js.org/loaders/)。  
main.jsx  

```jsx
// main.jsx
const React = require('react');
const ReactDOM = require('react-dom');

ReactDOM.render(
  <h1>Hello, world!</h1>,
  document.querySelector('#wrapper')
);
```

index.html

```html
<html>
  <body>
    <div id="wrapper"></div>
    <script src="bundle.js"></script>
  </body>
</html>
```

webpack.config.js  

```js
module.exports = {
  entry: './main.jsx',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        // test 是正则表达式
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            // 需要预置插件才能翻译至es2015 和react
            presets: ['es2015', 'react']
          }
        }
      }
    ]
  }
};
```

上面的代码段需要`babel-loader` 的预置插件才能运行：[babel-preset-es2015](https://www.npmjs.com/package/babel-preset-es2015)、[babel-preset-react](https://www.npmjs.com/package/babel-preset-react)  

## CSS 加载器 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo04))  

`webpack` 允许js 文件包含css 样式，然后通过[`css 加载器`](https://github.com/webpack-contrib/css-loader)进行处理。  

main.js

```js
require('./app.css');
```

app.css  

```css
body {
  background-color: blue;
}
```

index.html  

```html
<html>
  <head>
    <script type="text/javascript" src="bundle.js"></script>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
```

webpack.config.js  

```js
module.exports = {
  entry: './main.js',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules:[
      {
        test: /\.css$/,
        // 译注：nmp i style-loader css-loader --dev-save
        use: [ 'style-loader', 'css-loader' ]
      },
    ]
  }
};
```

注意，这里必须要用两个加载器。`css-loader` 用于读取css 文件，[`style-loader`](https://www.npmjs.com/package/style-loader)会向html 插入`<stylr>` 标签。*译注：译者测试好像已经不会在html 页面插入样式标签了，但不影响最终结果*  
然后启动服务。  

```bash
#
$ cd demo04
$ npm run dev
```  

实际上，`webpack` 会在`index.html` 插入内联样式。  

```html
<head>
  <script type="text/javascript" src="bundle.js"></script>
  <!-- 但是译者测试并没有内联样式，显示效果是一样的 -->
  <style type="text/css">
    body {
      background-color: blue;
    }
  </style>
</head>
```

## 图片加载器 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo05))  

## CSS 模块 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo06))  

## UglifyJs 插件 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo07))  

## HTML 插件与OpenBrowser 插件 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo08))  

## 环境标识 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo09))  

## 代码拆分 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo10))  

## 利用Babel 加载器进行代码拆分 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo11))  

## 公共代码块 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo12))  

## 自有代码块 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo13))  

## 全局公开变量 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo14))  

## React 路由] ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo15))  
