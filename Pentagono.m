function [in, xv, yv] = Pentagono(R,x0,y0,theta0)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
% Parámetros del pentágono
R = 5;           % Radio (tamaño)
h = x0; k = y0;    % Posición del centro (desplazamiento en x, y)
  % Rotación inicial

% Definir los vértices del pentágono
theta = linspace(0, 2*pi, 6); 
xv = h + R * cos(theta + theta0);
yv = k + R * sin(theta + theta0);

% Crear una malla de puntos en el espacio
[x, y] = meshgrid(h-1.2*R:0.1:h+1.2*R, k-1.2*R:0.1:k+1.2*R);

% Verificar qué puntos están dentro del pentágono
in = inpolygon(x, y, xv, yv); % Función MATLAB para ver si un punto está dentro de un polígono

% Graficar el pentágono como una región
figure;
hold on;
contourf(x, y, in, 1, 'LineColor', 'none'); % Rellenar con color
plot(xv, yv, 'r-', 'LineWidth', 2); % Borde del pentágono
colormap([0 0 1]); % Azul
axis equal;
grid on;
xlabel('x'); ylabel('y');
title('Región Convexa: Pentágono');

end