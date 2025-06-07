def heap_sort(arr):
    n = len(arr)

    # Construir el max-heap
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Intercambiar
        heapify(arr, i, 0)
    
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Ejemplo con npumeros negativos y positivos
mixed_nums = [-5, 10, -3, 8, -7, 4, 1]
print("\nHead Sort - Antes: ", mixed_nums)
heap_sort(mixed_nums)
print("Head Sort - Después: ", mixed_nums)



# Modificamos para ordenar por atributos
def heapify_tuples(arr, n, i, key=None):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Función comparación genérica
    def compare(a,b):
        if key:
            a_val = key(a)
            b_val = key(b)
            return a_val < b_val
        return a < b
    
    if l < n and compare(arr[largest], arr[l]):
        largest = l
    
    if r < n and compare(arr[largest], arr[r]):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_tuples(arr, n, largest, key)

def heap_sort_tuples(arr, key=None):
    n = len(arr)

    # Construir max-heap
    for i in range(n//2-1, -1, -1):
        heapify_tuples(arr, n, i, key)

    # Extraer elementos un opor uno
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_tuples(arr, i, 0, key)
    return arr

# Ejemplo con tuplas
tuples = [(1, "b"), (2, "a"), (1, "a"), (2, "b")]
print("\nTuplas antes: ", tuples)
heap_sort_tuples(tuples, key=lambda x: (x[0], x[1]))
print("Tuplas Después: ", tuples)
