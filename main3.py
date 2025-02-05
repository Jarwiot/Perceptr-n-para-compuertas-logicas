import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
import tkinter as tk
from tkinter import messagebox, filedialog

# Listas para almacenar las coordenadas y etiquetas
points = []
labels = []

# Función para manejar clics del mouse
def on_click(event):
    if event.button == 1:  # Clic izquierdo (clase 0, rosa)
        points.append([event.xdata, event.ydata])
        labels.append(0)
        color = 'pink'
    elif event.button == 3:  # Clic derecho (clase 1, azul)
        points.append([event.xdata, event.ydata])
        labels.append(1)
        color = 'blue'
    else:
        return  # Ignorar otros clics

    # Dibujar el punto
    plt.scatter(event.xdata, event.ydata, color=color)
    plt.draw()

# Función para guardar los datos
def save_data():
    if not points or not labels:
        messagebox.showwarning("Advertencia", "No hay datos para guardar.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".npz",
                                             filetypes=[("Archivo NPZ", "*.npz")],
                                             title="Guardar datos")
    if file_path:
        np.savez(file_path, points=np.array(points), labels=np.array(labels))
        messagebox.showinfo("Éxito", f"Datos guardados en {file_path}")

# Función para configurar y entrenar la red neuronal
def setup_and_train():
    # Obtener configuración de la interfaz
    try:
        num_layers = int(num_layers_entry.get())
        neurons_per_layer = list(map(int, neurons_entry.get().split(',')))
        if len(neurons_per_layer) != num_layers:
            raise ValueError("El número de capas y la configuración de neuronas no coinciden.")
    except ValueError as e:
        messagebox.showerror("Error", f"Error en la configuración: {e}")
        return

    # Dividir los datos
    points_np = np.array(points, dtype=np.float32)  # Asegurar tipo float32
    labels_np = np.array(labels, dtype=np.float32)  # Asegurar tipo float32
    if len(points_np) == 0:
        messagebox.showerror("Error", "No hay datos para entrenar.")
        return

    X_train, X_test, y_train, y_test = train_test_split(points_np, labels_np, test_size=0.3, random_state=42)

    # Crear el modelo
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=(2,)))
    for neurons in neurons_per_layer:
        model.add(tf.keras.layers.Dense(neurons, activation='tanh'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.03),
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    # Entrenar el modelo
    model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0)

    # Evaluar el modelo
    loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
    messagebox.showinfo("Resultado", f"Precisión en datos de prueba: {accuracy * 100:.2f}%")

    # Visualizar límites de decisión
    xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 300), np.linspace(-1.5, 1.5, 300))
    grid = np.c_[xx.ravel(), yy.ravel()]
    predictions = model.predict(grid).reshape(xx.shape)

    plt.contourf(xx, yy, predictions, levels=[0, 0.5, 1], cmap="RdBu", alpha=0.6)
    plt.scatter(points_np[:, 0], points_np[:, 1], c=labels_np, cmap="RdBu", edgecolor="white")
    plt.title("Límites de decisión de la red neuronal")
    plt.show()

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Red Neuronal Interactiva")

# Botón para iniciar la visualización y recolección de datos
start_btn = tk.Button(root, text="Recolectar puntos", command=lambda: plt.show())
start_btn.pack(pady=10)

# Entradas para la configuración de la red neuronal
config_frame = tk.Frame(root)
config_frame.pack(pady=10)

tk.Label(config_frame, text="Número de capas ocultas:").grid(row=0, column=0, padx=5, pady=5)
num_layers_entry = tk.Entry(config_frame)
num_layers_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(config_frame, text="Neuronas por capa (separadas por coma):").grid(row=1, column=0, padx=5, pady=5)
neurons_entry = tk.Entry(config_frame)
neurons_entry.grid(row=1, column=1, padx=5, pady=5)

# Botones de acción
action_frame = tk.Frame(root)
action_frame.pack(pady=10)

save_btn = tk.Button(action_frame, text="Guardar puntos", command=save_data)
save_btn.grid(row=0, column=0, padx=10)

train_btn = tk.Button(action_frame, text="Entrenar red neuronal", command=setup_and_train)
train_btn.grid(row=0, column=1, padx=10)

# Crear la figura y conectar el manejador de eventos
fig, ax = plt.subplots()
ax.set_title("Haz clic para agregar puntos (izq: rosa, der: azul)")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

cid = fig.canvas.mpl_connect('button_press_event', on_click)

# Iniciar la aplicación
root.mainloop()