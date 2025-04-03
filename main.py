import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from shapely.geometry import Point, Polygon as ShapelyPolygon

def generar_pentagono(R, h, k, theta0, grid_res):
    """
    Genera un conjunto convexo en forma de pentágono en una malla.

    Parámetros:
    - R: Radio del pentágono.
    - h, k: Coordenadas del centro.
    - theta0: Rotación inicial en radianes.
    - grid_res: Resolución de la malla.

    Retorna:
    - X, Y: Coordenadas de la malla.
    - inside: Matriz booleana indicando qué puntos están dentro del pentágono.
    - pentagono: Objeto ShapelyPolygon del pentágono.
    """
    # Generar los vértices del pentágono
    theta = np.linspace(0, 2*np.pi, 6)[:-1]  # 5 puntos
    x_v = h + R * np.cos(theta + theta0)
    y_v = k + R * np.sin(theta + theta0)
    
    # Crear el polígono de Shapely
    pentagono = ShapelyPolygon(np.c_[x_v, y_v])

    # Crear malla de puntos
    x_min, x_max = h - 1.2*R, h + 1.2*R
    y_min, y_max = k - 1.2*R, k + 1.2*R
    if x_min<0 or y_min<0:raise Exception("This set does not belong to the positive real number set")
    X, Y = np.meshgrid(np.arange(x_min, x_max, grid_res),
                       np.arange(y_min, y_max, grid_res))

    # Verificar qué puntos están dentro del pentágono
    inside = np.array([[pentagono.contains(Point(x, y)) for x in X[0]] for y in Y[:, 0]])

    return X, Y, inside, pentagono

def graficar_pentagono(X, Y, inside, pentagono,x_p,y_p):
    """
    Grafica el pentágono como una región convexa.
    """
    fig, ax = plt.subplots()
    ax.contourf(X, Y, inside, levels=1, colors=['blue'], alpha=0.5)
    ax.add_patch(Polygon(np.array(pentagono.exterior.coords), fill=None, edgecolor='red', linewidth=2))
    ax.scatter(x_p, y_p, color='blue', s=100, marker='o', label="Punto") 
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Región Convexa: Pentágono')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def punto_en_pentagono(pentagono, x_p, y_p):
    """
    Verifica si un punto está dentro del pentágono.
    """
    return pentagono.contains(Point(x_p, y_p))
def Minimum(X,Y,inside):
    min=10000000000000000000000000000000000000000000000000000000000000000000000000000000
    xmin=0
    ymin=0
    i=0

    while i<len(X):
        j=0
        while j<len(Y):
            x = X[i,j];y=Y[i,j]
            f = x*y
            if f<min and inside[i,j]:  min = f ; xmin =x ; ymin=y

            j+=1
        i+=1
    return min,xmin,ymin
    

numIteraciones = 5
iter = 0

while iter <=numIteraciones:

    X, Y, inside, pentagono = generar_pentagono(R=5, h=7+iter, k=8+iter, theta0=np.pi/4+np.pi*iter/8, grid_res=0.1)

    minimo,xmin,ymin = Minimum(X,Y,inside)

    print(f'El mínimo de la funcion es {minimo} y se encuentra en la coordenada ({xmin},{ymin})')
    graficar_pentagono(X, Y, inside, pentagono,xmin,ymin)
    iter+=1