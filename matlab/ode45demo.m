% y''=-t*y + e^t*y' +3sin2t
% 原文链接：https://blog.csdn.net/loggsy/article/details/80791924  

function ode45demo
    % 求解区间
    tspan=[3.9 4.0];
    % 初值
    y0=[8 2]; 
    % 解方程
    [t,x]=ode45(@odefun,tspan,y0);
    % 绘图
    plot(t,x(:,1),'-o',t,x(:,2),'-*')
    legend('y1','y2')
    title('y''''=-t*y + e^t*y'' +3sin2t')
    xlabel('t')
    ylabel('y')
    % 方程定义
    function y=odefun(t,x)
        % 2×1 的列向量
        y=zeros(2,1); 
        % 初值
        y(1)=x(2);
        % 方程
        y(2)=-t*x(1)+exp(t)*x(2)+3*sin(2*t); %常微分方程公式
    end
end