
import numpy as np
import matplotlib.pyplot as plt

# Variables globales
points = []  # Lista de puntos
w1, w2, bias = 0, 0, 0  # Pesos iniciales
classified = False  # Estado de clasificación

def perceptron_classify(x1, x2):
    """Clasifica el punto usando la ecuación del perceptrón."""
    return 1 if (w1 * x1 + w2 * x2 + bias) >= 0 else 0

def onclick(event):
    """Maneja los clics del mouse para agregar puntos."""
    global points, classified
    if event.xdata is not None and event.ydata is not None and not classified:
        points.append((event.xdata, event.ydata, 'black'))
        redraw()

def classify_points():
    """Clasifica los puntos según el perceptrón y cambia su color."""
    global points, classified
    if classified:
        return
    
    for i in range(len(points)):
        x1, x2, _ = points[i]
        color = 'blue' if perceptron_classify(x1, x2) else 'red'
        points[i] = (x1, x2, color)
    classified = True
    redraw()

def plot_hyperplane():
    """Grafica la línea de decisión del perceptrón."""
    if w2 == 0:
        return
    
    x_vals = np.linspace(-10, 10, 100)
    y_vals = (-w1 * x_vals - bias) / w2
    plt.plot(x_vals, y_vals, 'green', linestyle='dashed', label='Hiperplano')

def redraw():
    """Redibuja la gráfica con los puntos y el hiperplano."""
    plt.clf()
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Perceptrón para Clasificación')
    
    for x1, x2, color in points:
        plt.scatter(x1, x2, color=color)
    
    if classified:
        plot_hyperplane()
    
    plt.legend()
    plt.draw()

def main():
    global w1, w2, bias
    
    w1 = float(input("Ingrese el peso w1: "))
    w2 = float(input("Ingrese el peso w2: "))
    bias = float(input("Ingrese el bias w0: "))
    
    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Perceptrón para Clasificación')
    plt.show()
    
    classify_points()
    plt.show()

if __name__ == "__main__":
    main()
