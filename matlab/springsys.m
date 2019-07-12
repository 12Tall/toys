% ��������
m=10;
k=2;
c=0;
clf;
ode2;

% ���׳�΢�ַ�����Ҫ��ת����һ��ode������
function ode2
    % �������
    tspan=[0 100];
    % ��ֵ
    y0=[0 2]; 
    % �ⷽ��
    [t,x]=ode45(@odefun,tspan,y0);
    % ��ͼ
    plot(t,x(:,1),'-o',t,x(:,2),'-*')
    legend('y1','y2')
    title('y''''=g-k*y/m-cy''')
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
        Fy(2)=10-20/10*y(1)-0.5*y(2); %��΢�ַ��̹�ʽ
    end
end