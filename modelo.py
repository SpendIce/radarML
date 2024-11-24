import tensorflow as tf

def crear_modelo():
    # Definición de la red neuronal
    entrada = tf.keras.layers.Dense(units=3, input_shape=[3])  # 3 entradas
    oculta1 = tf.keras.layers.Dense(units=6, activation='relu')  # Capa oculta con 6 neuronas
    oculta2 = tf.keras.layers.Dense(units=6, activation='relu')  # Segunda capa oculta
    salida = tf.keras.layers.Dense(units=2)  # 2 salidas (movimiento, distancia futura)

    modelo = tf.keras.Sequential([entrada, oculta1, oculta2, salida])
    return modelo

def entrenar_modelo(modelo, datos_entrada, etiquetas_salida):

    # Compilación del modelo
    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )

    # Entrenamiento
    print("Comenzando el entrenamiento...\n")
    historial = modelo.fit(datos_entrada, etiquetas_salida, epochs=500, verbose=False)
    print("¡Entrenamiento finalizado!\n")
    return historial