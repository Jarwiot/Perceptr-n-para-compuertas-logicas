
import numpy as np
import matplotlib.pyplot as plt

# Función de activación (step function)
def step_function(z):
    return 1 if z >= 0 else 0

# Función para calcular la salida del perceptrón
def perceptron_output(x1, x2, w1, w2, bias):
    z = x1 * w1 + x2 * w2 + bias
    return step_function(z)

# Función para graficar el hiperplano
def plot_hyperplane(w1, w2, bias, x_range):
    m = -w1 / w2
    c = -bias / w2
    plt.plot(x_range, m * x_range + c, 'r--', label='Hiperplano de decisión')

# Función principal
def main():
    # Listas para almacenar los puntos (x1, x2)
    points = []
    labels = []

    # Solicitar al usuario que ingrese los pesos y el bias
    w1 = float(input("Ingrese el valor de w1: "))
    w2 = float(input("Ingrese el valor de w2: "))
    bias = float(input("Ingrese el valor del bias (w0): "))

    # Crear un gráfico interactivo para ingresar puntos con el mouse
    print("Haz clic en el gráfico para ingresar puntos. Presiona 'enter' para terminar.")
    fig, ax = plt.subplots()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.grid(True)
    ax.set_title("Ingresa puntos con el mouse")

    def onclick(event):
        if event.inaxes:
            x1, x2 = event.xdata, event.ydata
            points.append((x1, x2))
            ax.plot(x1, x2, 'ko')  # Graficar el punto en negro
            plt.draw()

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    # Clasificar los puntos ingresados
    for x1, x2 in points:
        label = perceptron_output(x1, x2, w1, w2, bias)
        labels.append(label)

    # Graficar los puntos clasificados
    fig, ax = plt.subplots()
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.grid(True)
    ax.set_title("Puntos clasificados")

    for (x1, x2), label in zip(points, labels):
        color = 'blue' if label == 1 else 'red'
        ax.plot(x1, x2, 'o', color=color)

    # Graficar el hiperplano de decisión
    x_range = np.array([-10, 10])
    plot_hyperplane(w1, w2, bias, x_range)
    ax.legend()
    plt.show()

if __name__ == "__main__":
    main()