# Redis 相关  

安装不多啰嗦 可自行百度  

## ASP.NET pending 问题  

- [x] ASP.NET WebApp 挂起  
    初步判断是`Redis` 中`Session` 存储冲突，导致后台进不到`.ashx`，一般问题只发生在应用重启时。可以在`Global.asax` 应用启动时清空下`Redis` 存储即可。
