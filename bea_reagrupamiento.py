import numpy as np

def bond(Ax, Ay, A):
    # Función para calcular el "bond" entre dos columnas Ax, Ay basado en la matriz de afinidad A
    return np.sum(A @ Ax * A @ Ay)

def calculate_cont(Ai, Ak, Aj, A):
    # Cálculo de la contribución según la fórmula proporcionada
    return 2 * bond(Ai, Ak, A) + 2 * bond(Ak, Aj, A) - 2 * bond(Ai, Aj, A)

def bea_algorithm(A):
    n, m = A.shape  # n: filas, m: columnas
    CA = np.zeros((n, m))  # Inicializar CA con ceros
    used_columns = [False] * m  # Rastrear columnas usadas
    column_order = []  # Para rastrear el orden de selección de columnas

    # Paso 1: Elegir la primera columna y colocarla en CA
    CA[:, 0] = A[:, 0]  # Fijando la primera columna
    used_columns[0] = True
    column_order.append(0)  # Agregar el índice de la columna seleccionada

    for i in range(1, m):  # Iterar para el resto de las columnas
        best_contribution = -np.inf
        best_column_index = -1
        best_position = -1

        for k in range(m):  # Para cada columna en A
            if used_columns[k]:
                continue  # Saltar columnas ya usadas
            for j in range(i):  # Encontrar la mejor posición (0 a i-1) en CA
                # Calcular contribución
                contribution = calculate_cont(CA[:, j], A[:, k], CA[:, 0], A)
                if contribution > best_contribution:
                    best_contribution = contribution
                    best_column_index = k
                    best_position = j

        # Colocar la mejor columna en CA
        CA[:, best_position + 1] = A[:, best_column_index]
        used_columns[best_column_index] = True
        column_order.append(best_column_index)  # Agregar el índice de la columna seleccionada

    # Reorganizar las filas en base al orden de las columnas seleccionadas
    CA_reorganized = CA.copy()
    for new_index, old_index in enumerate(column_order):
        CA_reorganized[:, new_index] = CA[:, old_index]

    return CA_reorganized

# Ejemplo de uso:
AA = np.array([[45, 0, 45, 0],
               [0, 80, 5, 75],
               [45, 5, 53, 3],
               [0, 75, 3, 78]])

# Ejecutar el algoritmo BEA
CA_resultante = bea_algorithm(AA)

# Mostrar el resultado
print("Matriz de afinidad agrupada CA:")
print(CA_resultante)
