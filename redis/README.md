# Redis 相关  

安装不多啰嗦 可自行百度  
## ASP.NET pending 问题  
RedisSessionStateProvider 在调试时会让后台.ashx 文件访问挂起，暂时不清除具体的原因，  
但是可以判断问题出在数据库或者dll 文件之一，在挂起发生后手动清空redis 数据库即可解决
