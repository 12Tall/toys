% ���Ʒ���
% ԭ�����ӣ�https://zhidao.baidu.com/question/435992701.html

% �����ͼ����
x = 0:0.2:6;
y = 0:0.1:2;
% ��������
[x,y] = meshgrid(x,y);
% ����y'=y(1-y);
fxy = y.*(1-y);
% ���ص�x,y���򳤶�
cosa = 1./(1+fxy.^2);
sina = cosa.*fxy;
% ���������
cla;
% ����ʸ��ͼ����ʼλ�ã�ʸ��
quiver(x,y,cosa,sina);
% ����
hold on
% �ⷽ�̣��������õ���������
[sx,sy] = ode45(@(x,y) y.*(1-y) ,[0,6],[0.2;1.8]);
% ��ͼ
plot(sx,sy,'r');