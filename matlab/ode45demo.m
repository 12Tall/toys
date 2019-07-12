% y''=-t*y + e^t*y' +3sin2t
% ԭ�����ӣ�https://blog.csdn.net/loggsy/article/details/80791924  

function ode45demo
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
    function y=odefun(t,x)
        % 2��1 ��������
        y=zeros(2,1); 
        % ��ֵ
        y(1)=x(2);
        % ����
        y(2)=-t*x(1)+exp(t)*x(2)+3*sin(2*t); %��΢�ַ��̹�ʽ
    end
end