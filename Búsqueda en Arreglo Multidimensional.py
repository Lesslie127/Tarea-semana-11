#matriz bidimensional (puede ser una matriz pequeña de 3x3)
# Matriz de ejemplo 3x3
matriz = [
    [2, 4, 6],
    [8, 3, 1],
    [7, 12, 16]
]
#Función que realice una búsqueda en la matriz para encontrar un valor específico
valor_a_buscar = 3
encontrado = False
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == valor_a_buscar:
            print(f"El valor {valor_a_buscar} se encontró en la posición [{i}][{j}] de la matriz.")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
