# 阮一峰《webpack-demos.md》 的翻译  

[本仓库](https://github.com/ruanyf/webpack-demos)由一系列`webpack` 的简单demo 组成。  
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

注意，这里必须要用两个加载器。`css-loader` 用于读取css 文件，[`style-loader`](https://www.npmjs.com/package/style-loader)会向html 插入`<style>` 标签。*译注：译者测试好像已经不会在html 页面插入样式标签了，但不影响最终结果*  
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

`webpack` 也可以在js 文件中包含图片文件。  

main.js  

```js
var img1 = document.createElement("img");
img1.src = require("./small.png");
document.body.appendChild(img1);

var img2 = document.createElement("img");
img2.src = require("./big.png");
document.body.appendChild(img2);
```  

index.html  

```html
<html>
  <body>
    <script type="text/javascript" src="bundle.js"></script>
  </body>
</html>
```  

webpack.config.js  

```js
// 需要 npm i url-loader --dev-save
module.exports = {
  entry: './main.js',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules:[
      {
        test: /\.(png|jpg)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 8192
            }
          }
        ]
      }
    ]
  }
};
```

[url-loader](https://www.npmjs.com/package/url-loader) 可以将图片文件转换成`<img/>` 标签，大小小于`8192kb` 时直接转化成`base64` 编码，否则插入正常的url。  

启动npm 服务后，大图片和小图片分别被加载为以下格式。  

```html
<img src="data:image/png;base64,iVBOR...uQmCC">
<img src="4853ca667a2b8b8844eb2693ac1b2578.png">
```

## CSS 模块 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo06))  

`css-loader?module`(查询参数模块)启用[`CSS 模块`](https://github.com/css-modules/css-modules)。为js 模块中的css 提供局部的作用域？我们也可以使用`:global(selector)`来将其关闭([详情](https://css-modules.github.io/webpack-demo/))  

*译注：其实上面这一段几乎完全没有看懂，但是从代码理解：react 中的局部样式与全局样式的打包*

index.html

```html
<html>
<body>
  <h1 class="h1">Hello World</h1>
  <h2 class="h2">Hello Webpack</h2>
  <div id="example"></div>
  <script src="./bundle.js"></script>
</body>
</html>
```

app.css

```css
/* 局部样式 */
.h1 {
  color:red;
}

/* 全局样式 */
:global(.h2) {
  color: blue;
}
```

main.jsx

```jsx
var React = require('react');
var ReactDOM = require('react-dom');
var style = require('./app.css');

ReactDOM.render(
  <div>
    <h1 className={style.h1}>Hello World</h1>
    <h2 className="h2">Hello Webpack</h2>
  </div>,
  document.getElementById('example')
);
```

webpack.config.js

```js
module.exports = {
  entry: './main.jsx',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules:[
      {
        test: /\.js[x]?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            // Error: Couldn't find preset "es2015" relative to directory
            // npm install --save-dev babel-preset-es2015
            // npm install --save-dev babel-preset-react
            presets: ['es2015', 'react']
          }
        }
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
             loader: 'css-loader',
             options: {
               modules: true
             }
          }
        ]
      }
    ]
  }
};
```

启动服务  

```bash
#
$ cd demo06
$ npm run dev
# 这里可能会出错
# 需要添加PATH 环境变量：C:\windows\system32
# https://stackoverflow.com/questions/28624686/get-spawn-cmd-enoent-when-try-to-build-cordova-application-event-js85
```

访问<http://127.0.0.1:8080/>，你会发现只有`h1`标签是红色的，因为它的样式是局部样式，两个`h2`都是蓝色的，因为它的样式是全局的。  
*译注：解决Error 也是蛮有成就感的*  

## UglifyJs 插件 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo07))  

Webpack 通过插件系统来扩展功能，例如[UglifyJs Plugin](https://webpack.js.org/plugins/uglifyjs-webpack-plugin/) 就可以压缩生成的js 代码(bundle.js)。  

main.js  

```js
var longVariableName = 'Hello';
longVariableName += ' World';
document.write('<h1>' + longVariableName + '</h1>');
```

index.html  

```html
<html>
<body>
  <script src="bundle.js"></script>
</body>
</html>
```

webpack.config.js

```js
var webpack = require('webpack');
var UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
  entry: './main.js',
  output: {
    filename: 'bundle.js'
  },
  plugins: [
    new UglifyJsPlugin()
  ]
};
```

在启动服务之后，main.js 的内容在bundle.js 内会被压缩成下面的样子  

```js
var o="Hello";o+=" World",document.write("<h1>"+o+"</h1>")
```

## HTML 插件与OpenBrowser 插件 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo08))  

通过此例，我们可以嘘唏如何加载第三方插件  

[html-webpack-plugin](https://github.com/ampedandwired/html-webpack-plugin) 会为我们自动创建`index.html`，同时[open-browser-webpack-plugin](https://github.com/baldore/open-browser-webpack-plugin) 在webpack 启动时会自动打开一个浏览器标签  

main.js  

```js
document.write('<h1>Hello World</h1>');
```

webpack.config.js

```js
var HtmlwebpackPlugin = require('html-webpack-plugin');
var OpenBrowserPlugin = require('open-browser-webpack-plugin');

module.exports = {
  entry: './main.js',
  output: {
    filename: 'bundle.js'
  },
  plugins: [
    new HtmlwebpackPlugin({
      title: 'Webpack-demos',
      filename: 'index.html'
    }),
    new OpenBrowserPlugin({
      url: 'http://localhost:8080'
    })
  ]
};
```

启动服务  

```bash
#
$ cd demo08
$ npm run dev
```

现在我们就无需手写index.html 了，webpack 也会自动帮我们打开浏览器标签  

## 环境标识 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo09))  

通过环境标识符，我们可以让某些代码只在开发时运行  
*译注：这个似乎是nodejs 自带的功能，非webpack 独有*

main.js

```js
document.write('<h1>Hello World</h1>');

if (__DEV__) {
  document.write(new Date());
}
```

index.html

```html
<html>
<body>
  <script src="bundle.js"></script>
</body>
</html>
```  

webpack.config.js

```js
var webpack = require('webpack');

var devFlagPlugin = new webpack.DefinePlugin({
  __DEV__: JSON.stringify(JSON.parse(process.env.DEBUG || 'false'))
});

module.exports = {
  entry: './main.js',
  output: {
    filename: 'bundle.js'
  },
  plugins: [devFlagPlugin]
};
```  

将环境变量传入webpack：打开package.json，通过script 属性就可以实现  

```js
// package.json
{
  // ...
  "scripts": {
    "dev": "cross-env DEBUG=true webpack-dev-server --open",
  },
  // ...
}
// 注：正式的package.json 中不要带注释
// 也不要添加无用的逗号
```  

启动服务  

```bash
#
$ cd demo09
$ npm run dev
```  

## 代码拆分 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo10))  

对于大型的webapp，所有代码放在一个js 文件里面效率过低。webpack 允许将js 源码拆分为若干代码块，按需加载  

webpack 利用[`require.ensure`](http://webpack.github.io/docs/code-splitting.html) 方法定义拆分节点  

```js
// main.js
require.ensure(['./a'], function (require) {
  var content = require('./a');
  document.open();
  document.write('<h1>' + content + '</h1>');
  document.close();
});
```

`require.ensure` 告知webpack `./a/js` 应当从bundle.js 中拆分成独立的代码块  

```js
// a.js
module.exports = 'Hello World';
```

现在由webpack 负责管理依赖、输出等各种东西，我们无需再关心`index.html` 和`webpack.config.js` 中的多余代码  

```html
<html>
  <body>
    <script src="bundle.js"></script>
  </body>
</html>
```

webpack.config.js

```js
module.exports = {
  entry: './main.js',
  output: {
    filename: 'bundle.js'
  }
};
```

启动服务  

```bash
#
$ cd demo10
$ npm run dev
```  

webpack 会将main.js 和a.js 构建为两个目标文件bundle.js 和0.bundle.js。在需要时加载0.bundle.js，但是我们感觉不出有任何区别  

## 利用Bundle 加载器进行代码拆分 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo11))  

代码拆分的另一种办法就是使用[bundle-loader](https://www.npmjs.com/package/bundle-loader)  

```js
// main.js

// Now a.js is requested, it will be bundled into another file
var load = require('bundle-loader!./a.js');

// To wait until a.js is available (and get the exports)
//  you need to async wait for it.
load(function(file) {
  document.open();
  document.write('<h1>' + file + '</h1>');
  document.close();
});
```

`require('bundle-loader!./a.js')` 告知webpack 从额外的代码块加载a.js  
webpack 会将main.js构建为bundle.js，a.js 构建为0.bundule.js  

## 公共代码块 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo12))  

当多个脚本拥有公共代码块的时候，webpack 可以通过[CommonsChunkPlugin](https://webpack.js.org/plugins/commons-chunk-plugin/) 提取公共部分到单独的文件。有利于浏览器缓存与节省带宽。  

```js
// main1.jsx
var React = require('react');
var ReactDOM = require('react-dom');

ReactDOM.render(
  <h1>Hello World</h1>,
  document.getElementById('a')
);

// main2.jsx
var React = require('react');
var ReactDOM = require('react-dom');

ReactDOM.render(
  <h2>Hello Webpack</h2>,
  document.getElementById('b')
);
```

index.html

```html
<html>
  <body>
    <div id="a"></div>
    <div id="b"></div>
    <script src="commons.js"></script>
    <script src="bundle1.js"></script>
    <script src="bundle2.js"></script>
  </body>
</html>
```

上文中，common.js 就是main1.jsx 和main2.jsx 的公共部分，包含了react 和react-dom。  

webpack.config.js  

```js
var webpack = require('webpack');

module.exports = {
  entry: {
    bundle1: './main1.jsx',
    bundle2: './main2.jsx'
  },
  output: {
    filename: '[name].js'
  },
  module: {
    rules:[
      {
        test: /\.js[x]?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['es2015', 'react']
          }
        }
      },
    ]
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin({
      name: "commons",
      // (the commons chunk name)

      filename: "commons.js",
      // (the filename of the commons chunk)
    })
  ]
}
```

## 自有代码块 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo13))  

通过`CommonsChunkPlugin` 我们还可以抽取出自己的代码块  

main.js  

```js
var $ = require('jquery');
$('h1').text('Hello World');
```

index.html

```html
<html>
  <body>
    <h1></h1>
    <script src="vendor.js"></script>
    <script src="bundle.js"></script>
  </body>
</html>
```

webpack.config.js  

```js
var webpack = require('webpack');

module.exports = {
  entry: {
    app: './main.js',
    vendor: ['jquery'],
  },
  output: {
    filename: 'bundle.js'
  },
  plugins: [
    new webpack.optimize.CommonsChunkPlugin({
      name: 'vendor',
      filename: 'vendor.js'
    })
  ]
};
```

上面的代码中，`entry.vendor: ['jquery']` 表示jQuery 需要被包含在公共代码块`vendor.js` 中  

如果需要将某个模块的变量，作为全局变量使用，并且不需要require。我们可以使用[ProvidePlugin](https://webpack.js.org/plugins/provide-plugin/)来自动载入模块。  

```js
// main.js
$('h1').text('Hello World');


// webpack.config.js
var webpack = require('webpack');

module.exports = {
  entry: {
    app: './main.js'
  },
  output: {
    filename: 'bundle.js'
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    })
  ]
};
```  

当然，我们需要在全局加载jquery.js

## 全局公开变量 ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo14))  

如果需要使用全局变量，并且不想再webpack 中包含他们，我们可以在`webpack.config.js`启用[`externals`](https://webpack.js.org/configuration/externals/) 字段。

例如，我们有一个data.js 文件  

```js
// data.js
var data = 'Hello World';
```  

index.html

```html
<html>
  <body>
    <script src="data.js"></script>
    <script src="bundle.js"></script>
  </body>
</html>
```

注意：webpack 只会打包bundle.js 而不会打包data.js。我们需要将data 作为全局变量暴露  

```js
// webpack.config.js
module.exports = {
  entry: './main.jsx',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules:[
      {
        test: /\.js[x]?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['es2015', 'react']
          }
        }
      },
    ]
  },
  externals: {
    // require('data') is external and available
    //  on the global var data
    'data': 'data'
  }
};
```

现在我们可以将data 当作模块变量引入，但其实他已经是全局变量了  

```js
// main.jsx
var data = require('data');
var React = require('react');
var ReactDOM = require('react-dom');

ReactDOM.render(
  <h1>{data}</h1>,
  document.body
);
```  

我们也可以将react 和react-dom 作为全局变量引入，此举将会大幅减少构建时间和输出文件大小  

## React 路由] ([源码](https://github.com/ruanyf/webpack-demos/tree/master/demo15))  

此例使用webpack 构建[React-router](https://github.com/rackt/react-router/blob/0.13.x/docs/guides/overview.md)官方示例  

一个带有仪表盘、收件箱和日历的小程序  

```txt
+---------------------------------------------------------+
| +---------+ +-------+ +--------+                        |
| |Dashboard| | Inbox | |Calendar|      Logged in as Jane |
| +---------+ +-------+ +--------+                        |
+---------------------------------------------------------+
|                                                         |
|                        Dashboard                        |
|                                                         |
|                                                         |
|   +---------------------+    +----------------------+   |
|   |                     |    |                      |   |
|   | +              +    |    +--------->            |   |
|   | |              |    |    |                      |   |
|   | |   +          |    |    +------------->        |   |
|   | |   |    +     |    |    |                      |   |
|   | |   |    |     |    |    |                      |   |
|   +-+---+----+-----+----+    +----------------------+   |
|                                                         |
+---------------------------------------------------------+
```

webpack.config.js  

```js
module.exports = {
  entry: './index.js',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['es2015', 'react']
          }
        }
      },
    ]
  }
};
```  

index.js

```js
import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';

import './app.css';

class App extends React.Component {
  render() {
    return (
      <div>
        <header>
          <ul>
            <li><Link to="/app">Dashboard</Link></li>
            <li><Link to="/inbox">Inbox</Link></li>
            <li><Link to="/calendar">Calendar</Link></li>
          </ul>
          Logged in as Jane
        </header>
        <main>
          <Switch>
            <Route exact path="/" component={Dashboard}/>
            <Route path="/app" component={Dashboard}/>
            <Route path="/inbox" component={Inbox}/>
            <Route path="/calendar" component={Calendar}/>
            <Route path="*" component={Dashboard}/>
          </Switch>
        </main>
      </div>
    );
  }
};

class Dashboard extends React.Component {
  render() {
    return (
      <div>
        <p>Dashboard</p>
      </div>
    );
  }
};

class Inbox extends React.Component {
  render() {
    return (
      <div>
        <p>Inbox</p>
      </div>
    );
  }
};

class Calendar extends React.Component {
  render() {
    return (
      <div>
        <p>Calendar</p>
      </div>
    );
  }
};

render((
  <BrowserRouter>
    <Route path="/" component={App} />
  </BrowserRouter>
), document.querySelector('#app'));
```  

index.html  

```html
<html>
  <body>
    <div id="app"></div>
    <script src="/bundle.js"></script>
  </body>
</htmL>
```  

启动服务  

```bash
#
$ cd demo15
$ npm run dev
```  

## 参考链接  

- [Webpack docs](https://webpack.js.org/concepts/)  
- [webpack-howto](https://github.com/petehunt/webpack-howto), by Pete Hunt  
- [SurviveJS Webpack book](https://survivejs.com/webpack/introduction/), by Juho Vepsäläinen  
- [Diving into Webpack](https://web-design-weekly.com/2014/09/24/diving-webpack/), by Web Design Weekly  
- [Webpack and React is awesome](http://www.christianalfoni.com/articles/2014_12_13_Webpack-and-react-is-awesome), by Christian Alfoni  
- [Browserify vs Webpack](https://medium.com/@housecor/browserify-vs-webpack-b3d7ca08a0a9), by Cory House  

## 许可  

MIT  

## 翻译后记  

语言是比较简单的，但是代码很多没有接触过，仓促之间学习前端还是有很多坑没有遇到过的。怎么才能理解别人呢，怎么才能被别人理解呢，翻译如果只是为了给自己看，那翻译又有什么意义呢？  
