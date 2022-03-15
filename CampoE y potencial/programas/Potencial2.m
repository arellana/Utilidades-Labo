function Potencial2()

Dx = dlmread('Potenciales/Potencial2.txt');
x = [1:2:22];
y = [1:2:20];

figure(1)

mesh(y,x,Dx,'FaceColor','interp');
colormap(jet)
colorbar
xlabel('\bf\fontsize{16}{X(cm)}')
ylabel('\bf\fontsize{16}{Y(cm)}')
zlabel('\bf\fontsize{16}{Tension(V)}')
set(gca,'fontsize',16)

Ex2 = dlmread('CamposDiscret/Ex2.txt');
Ey2 = dlmread('CamposDiscret/Ey2.txt');
x = [1:1:8];
y = [1:1:9];


[xx,yy] = meshgrid(x,y);

figure(2)
quiver(Ey2,Ex2);

  