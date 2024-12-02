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
def calcular_matriz_afinidad(query_attr, query_access):
    num_atributos = query_attr.shape[1]
    aa_matrix = np.zeros((num_atributos, num_atributos))
    
    for i in range(num_atributos):
        for j in range(num_atributos):
            if i == j:  # Diagonal principal: afinidad de un atributo consigo mismo
                consultas_con_attr = np.where(query_attr[:, i] == 1)[0]
                aa_matrix[i, j] = np.sum(query_access[consultas_con_attr, :])
            else:  # Afinidad entre atributos distintos
                consultas_con_both_attrs = np.where((query_attr[:, i] == 1) & (query_attr[:, j] == 1))[0]
                aa_matrix[i, j] = np.sum(query_access[consultas_con_both_attrs, :])
    
    return aa_matrix

# Main program para generar las matrices
if __name__ == "__main__":
    # Solicitar matrices de uso y acceso
    query_attr = solicitar_matriz("de uso")

    query_access = solicitar_matriz("de acceso")

    # Generar la matriz de afinidad
    aa_matrix = calcular_matriz_afinidad(query_attr, query_access)

    print("\nMatriz de Afinidad (AA) generada:")
    print(aa_matrix)
