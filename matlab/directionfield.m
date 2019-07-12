% 绘制方向场
% 原文链接：https://zhidao.baidu.com/question/435992701.html

% 定义绘图区域
x = 0:0.2:6;
y = 0:0.1:2;
% 绘制网格
[x,y] = meshgrid(x,y);
% 方程y'=y(1-y);
fxy = y.*(1-y);
% 线素的x,y方向长度
cosa = 1./(1+fxy.^2);
sina = cosa.*fxy;
% 清除坐标区
cla;
% 绘制矢量图：起始位置，矢量
quiver(x,y,cosa,sina);
% 保持
hold on
% 解方程：这里是用的匿名函数
[sx,sy] = ode45(@(x,y) y.*(1-y) ,[0,6],[0.2;1.8]);
% 画图
plot(sx,sy,'r');