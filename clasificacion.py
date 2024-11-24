def clasificar_movimiento(movimiento):
    # Clasificación del movimiento
    if -0.95 < movimiento < 0.95 and abs(movimiento) > 0.1:  # Lento
        movimiento_clasificado = "Lento"
    elif abs(movimiento) >= 1:  # Rápido
        movimiento_clasificado = "Rápido"
    else:  # Fijo
        movimiento_clasificado = "Fijo"
    return movimiento_clasificado

def mostrar_resultados(movimiento_clasificado, distancia_futura):
    print("\nPredicción:")
    print(f"Movimiento clasificado: {movimiento_clasificado}")
    print(f"Movimiento: {movimiento_clasificado}")
    print(f"Distancia futura (3 s): {distancia_futura:.2f} mm")