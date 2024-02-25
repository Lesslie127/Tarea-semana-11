#Programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).
#Función QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Matriz de ejemplo 3x3
matriz = [
    [9, 5, 7],
    [1, 3, 2],
    [8, 4, 6]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

#Ordenar una fila específica
fila_a_ordenar = 1  #Segunda fila
matriz[fila_a_ordenar] = quicksort(matriz[fila_a_ordenar])

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila", fila_a_ordenar, "ordenada:")
for fila in matriz:
    print(fila)
