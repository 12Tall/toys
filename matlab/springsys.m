% 常数定义
m=10;
k=2;
c=0;
clf;
ode2;

% 二阶常微分方程需要先转换成一阶ode方程组
function ode2
    % 求解区间
    tspan=[0 100];
    % 初值
    y0=[0 2]; 
    % 解方程
    [t,x]=ode45(@odefun,tspan,y0);
    % 绘图
    plot(t,x(:,1),'-o',t,x(:,2),'-*')
    legend('y1','y2')
    title('y''''=g-k*y/m-cy''')
    xlabel('t')
    ylabel('y')
    % 方程定义
    % F(y)=-t*y + e^t*y' +3sin2t
    function Fy=odefun(t,y)
        % 令Fy(1) = y
        % 令Fy(2) = y'
        
        % 2×1 的列向量
        Fy=zeros(2,1); 
        
        % y(1)'=y(2)
        Fy(1)=y(2);
        % y(2)'=表达式
        Fy(2)=10-20/10*y(1)-0.5*y(2); %常微分方程公式
    end
end