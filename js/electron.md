# electron踩坑  

[参考链接一](https://juncaixinchi.github.io/Blogs/2017/11/13/electron-101/)  
[robotjs](http://robotjs.io/docs/electron)  

## 安装  

- 通过`cnpm` 可以安装  
- 也可以通过`npm` 使用淘宝镜像安装  

```bash
npm install electron --registry=https://registry.npm.taobao.org
```

## 编译二进制包  

```bash
*** was compiled against a different Node.js version using
NODE_MODULE_VERSION **. This version of Node.js requires
NODE_MODULE_VERSION **. Please try re-compiling or re-installing
the module
```  

原因是`electron` 编译的node 版本与`npm install` 使用的版本不一致，可能`electron` 的node 版本没有对应的node 官方发行版，所以需要`rebuild`  

```bash
npm i --save-dev electron-rebuild
# 注意Windows 下的分隔符问题 \/
node_modules/.bin/electron-rebuild
```

cnpm 安装的包可能不能通过编译  

