function Potencial1()

Dx = dlmread('Potenciales/Potencial1.txt');
x = [1:2:22];
y = [1:2:20];

figure(1)

mesh(y,x,Dx,'FaceColor','interp');
colormap(jet(500))
colorbar
xlabel('\bf\fontsize{16}{X(cm)}')
ylabel('\bf\fontsize{16}{Y(cm)}')
zlabel('\bf\fontsize{16}{Tension(V)}')
set(gca,'fontsize',16)

Ex1 = dlmread('CamposDiscret/Ex1.txt');
Ey1 = dlmread('CamposDiscret/Ey1.txt');
x = [1:2:16];
y = [1:2:18];



[xx,yy] = meshgrid(x,y);

figure(2)
quiver(Ey1,Ex1);

