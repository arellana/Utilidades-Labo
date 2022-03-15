function Potencial3()

Dx = dlmread('Potenciales/Potencial3.txt');
x = [1:1:11];
y = [1:1:10];

figure(1)

mesh(y,x,Dx,'FaceColor','interp');
colormap(jet(500))
colorbar
xlabel('\bf\fontsize{16}{X(cm)}')
ylabel('\bf\fontsize{16}{Y(cm)}')
zlabel('\bf\fontsize{16}{Tension(V)}')
set(gca,'fontsize',16)

Ex3 = dlmread('CamposDiscret/Ex3.txt');
Ey3 = dlmread('CamposDiscret/Ey3.txt');
x = [1:1:8];
y = [1:1:9];

figure(2)

[xx,yy] = meshgrid(x,y);

quiver(Ey3,Ex3);
