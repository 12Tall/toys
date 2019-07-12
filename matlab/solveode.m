% solveode

dsolve('Dy=3*x*x','x');
dsolve('Dy=3*x*x','y(0)=2','x');
ode1;
ode2;

function ode1
    % 绘图区间与初值
    tspan=[0 40];
    y0=2; 
    % 解方程
    [t,x]=ode45(@odefun1,tspan,y0);
    % 绘图
    plot(t,x(:,1),'-o')
    legend('y')
    title('y''=3*x^2')
    xlabel('x')
    ylabel('y')
    
    function dYdx=odefun1(x,y)
        dYdx=3*x^2;
    end
end

% 二阶常微分方程需要先转换成一阶ode方程组
function ode2
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
    % F(y)=-t*y + e^t*y' +3sin2t
    function Fy=odefun(t,y)
        % 令Fy(1) = y
        % 令Fy(2) = y'
        
        % 2×1 的列向量
        Fy=zeros(2,1); 
        
        % y(1)'=y(2)
        Fy(1)=y(2);
        % y(2)'=表达式
        Fy(2)=-t*y(1)+exp(t)*y(2)+3*sin(2*t); %常微分方程公式
    end
end




