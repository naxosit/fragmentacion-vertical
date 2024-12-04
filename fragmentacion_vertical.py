# Código extraído del link: https://github.com/SyedMuhammadMuhsinKarim/Bond-Energy-Algorithm/blob/master/README.md

import numpy as np

# Solicitar matrices iniciales al usuario
def solicitar_matriz(nombre):
    print(f"Ingrese la matriz {nombre} (separando los elementos por espacios y las filas por saltos de línea):")
    matriz = []
    while True:
        fila = input()
        if fila == "":
            break
        matriz.append(list(map(int, fila.split())))
    return np.array(matriz)

# Calcular la matriz de afinidad
def calcular_matriz_afinidad(query_attr, query_access, acceso_ejecucion):
    num_atributos = query_attr.shape[1]
    aa_matrix = np.zeros((num_atributos, num_atributos))
    
    for i in range(num_atributos):
        for j in range(num_atributos):
            if i == j:  # Diagonal principal: afinidad de un atributo consigo mismo
                consultas_con_attr = np.where(query_attr[:, i] == 1)[0]
                aa_matrix[i, j] = np.sum(query_access[consultas_con_attr, :] * acceso_ejecucion)
            else:  # Afinidad entre atributos distintos
                consultas_con_both_attrs = np.where((query_attr[:, i] == 1) & (query_attr[:, j] == 1))[0]
                aa_matrix[i, j] = np.sum(query_access[consultas_con_both_attrs, :] * acceso_ejecucion)
    
    return aa_matrix

# Uniremos el otro código para que se ejecute en el mismo script

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

    # Paso 1: Elegir la primera columna y colocarla en CA
    CA[:, 0] = A[:, 0]  # Fijando la primera columna
    used_columns[0] = True

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

    return CA

def reorganizar_filas(CA):
    n, m = CA.shape
    orden_columnas = []
    for j in range(m):
        col = CA[:, j]
        for k in range(m):
            if np.array_equal(col, aa_matrix[:, k]):
                orden_columnas.append(k)
                break
    
    CA_reorganizada = np.zeros_like(CA)
    for i, idx in enumerate(orden_columnas):
        CA_reorganizada[i, :] = CA[idx, :]
    
    return CA_reorganizada

# Main program para generar las matrices
if __name__ == "__main__":
    # Solicitar matrices de uso y acceso
    query_attr = solicitar_matriz("de uso")

    
    query_access = solicitar_matriz("de acceso")

    # Solicitar el valor de acceso/ejecución
    acceso_ejecucion = float(input("\nIngrese el valor de acceso/ejecución: "))

    # Generar la matriz de afinidad
    aa_matrix = calcular_matriz_afinidad(query_attr, query_access, acceso_ejecucion)

    print("\nMatriz de Afinidad (AA) generada:")
    print(aa_matrix)


    CA_resultante = bea_algorithm(aa_matrix)
    # Reorganizar las filas de CA 
    CA_resultante_2 = reorganizar_filas(CA_resultante)
    # Mostrar el resultado
    print("Matriz de afinidad agrupada CA:")
    print(CA_resultante)

    # Mostrar el resultado
    print("Matriz de afinidad agrupada CA reorganizada:")
    print(CA_resultante_2)

# Codigo correspondiente a G2, Base de datos avanzadas