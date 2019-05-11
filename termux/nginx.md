# nginx  

- [x]  could not accessed from internet?!  

> should install [hskTurnnel for android] first.  

## nginx config  

> `nginx` must be used to start the service after installed  
> `/etc/nginx/`:there are some configuration files  
> root path:`/data/data/com.termux/files
/usr/share/nginx/html`  
> after system start or reboot, you should change directory to `/etc/nginx/`, and then execute the directive `nginx`  

### proxy_pass  

**摘自**[博客园](https://www.cnblogs.com/kevingrace/p/6566119.html)  

主要差别是url 加不加`/`  
url:`http://192.168.1.23/proxy/index.html`  

```nginx  
# 从机配置
# exp1:  
location /proxy/ {
        proxy_pass http://192.168.1.5:8090/;
        # 访问http://192.168.23/proxy/ 会被代理到http://192.168.1.5:8090/
        # 页面访问http://192.168.23/proxy 时会自动加上'/'
}
# exp2:
location /proxy/ {
        proxy_pass http://192.168.1.5:8090;
        # 访问http://192.168.1.23/proxy/ 会被代理
        # 到http://192.168.1.5:8090/proxy/
        # 而访问http://192.168.1.23/proxy 会失败
}
# exp3:
location /proxy/ {
        proxy_pass http://192.168.1.5:8090/path/;
        # 访问http://192.168.1.23/proxy/ 会被代理
        # 到http://192.168.1.5:8090/path/
        # 类似于第一种情况
}
# exp4:
location /proxy/ {
        proxy_pass http://192.168.1.5:8090/path;
        # 访问http://192.168.1.23/proxy/index.html 会被
        # 代理到http://192.168.1.5:8090/pathindex.html
        # 注意，这种情况下，不能直接访问http://192.168.1.23/proxy/
        # 后面就算是默认的index.html文件也要跟上，否则访问失败！
}
```

看需求来吧，感觉`nginx` 可以单独拉出来了  

```nginx  
# 主机配置
# exp1:
location /proxy {
        proxy_pass http://192.168.1.5:8090/;
        # 访问http://192.168.1.23/proxy 会被代理到http://192.168.1.5:8090/
        # 访问http://192.168.1.23/proxy/ 会被代理到http://192.168.1.5:8090/
}
# exp2:
location /proxy {
        proxy_pass http://192.168.1.5:8090;
        # 访问http://192.168.1.23/proxy 会自动加上'/'
        # 然后被代理到http://192.168.1.5:8090/proxy/
}
# exp3:
location /proxy {
        proxy_pass http://192.168.1.5:8090/path/;
        # 访问http://192.168.1.23/proxy 会自动加上'/'
        # 然后被代理到http://192.168.1.5:8090/path/
}
# exp4:
location /proxy {
        proxy_pass http://192.168.1.5:8090/path;
        # 访问http://192.168.1.23/proxy 会自动加上'/'
        # 然后被代理到http://192.168.1.5:8090/path/
        # 同第三种情况
}

```