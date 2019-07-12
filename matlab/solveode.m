% solveode

dsolve('Dy=3*x*x','x');
dsolve('Dy=3*x*x','y(0)=2','x');
ode1;
ode2;

function ode1
    % ��ͼ�������ֵ
    tspan=[0 40];
    y0=2; 
    % �ⷽ��
    [t,x]=ode45(@odefun1,tspan,y0);
    % ��ͼ
    plot(t,x(:,1),'-o')
    legend('y')
    title('y''=3*x^2')
    xlabel('x')
    ylabel('y')
    
    function dYdx=odefun1(x,y)
        dYdx=3*x^2;
    end
end

% ���׳�΢�ַ�����Ҫ��ת����һ��ode������
function ode2
    % �������
    tspan=[3.9 4.0];
    % ��ֵ
    y0=[8 2]; 
    % �ⷽ��
    [t,x]=ode45(@odefun,tspan,y0);
    % ��ͼ
    plot(t,x(:,1),'-o',t,x(:,2),'-*')
    legend('y1','y2')
    title('y''''=-t*y + e^t*y'' +3sin2t')
    xlabel('t')
    ylabel('y')
    % ���̶���
    % F(y)=-t*y + e^t*y' +3sin2t
    function Fy=odefun(t,y)
        % ��Fy(1) = y
        % ��Fy(2) = y'
        
        % 2��1 ��������
        Fy=zeros(2,1); 
        
        % y(1)'=y(2)
        Fy(1)=y(2);
        % y(2)'=���ʽ
        Fy(2)=-t*y(1)+exp(t)*y(2)+3*sin(2*t); %��΢�ַ��̹�ʽ
    end
end




