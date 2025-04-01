function [inside] = Circumference(R,x0,y0)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
[x, y] = meshgrid(-(R-x0):0.1:(R-x0), -(R-x0):0.1:(R-x0)); % Malla de puntos
 % Radio

% Matriz lógica que define el conjunto convexo
inside = ((x-x0).^2 + (y-y0).^2) <= R^2;

% Graficamos el conjunto
figure;
hold on;
contourf(x, y, inside, 1, 'LineColor', 'none'); % Rellena la circunferencia
colormap([0 0 1]); % Color azul
axis equal;
grid on;
xlabel('x'); ylabel('y');
title('Conjunto convexo: Disco dentro de la circunferencia');
end