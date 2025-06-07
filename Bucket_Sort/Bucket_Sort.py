def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr
    
    # Encontrar valores mínimo y máximo
    min_val = min(arr)
    max_val = max(arr)

    # Crear cubetas
    bucket_count = int((max_val - min_val) / bucket_size) + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribuir elementos en cubetas
    for num in arr:
        index = int((num -min_val) / bucket_size)
        buckets[index].append(num)

    # Ordenas cubetas y concatenar
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)  # Puede usarse cualquier algoritmo
        sorted_arr.extend(bucket)

    return sorted_arr

# Ejemplos con números flotantes
float_nums = [0.9982, 0.3245, 0.1829, 0.3204, 0.5684, 0.7496]
print("\nBucket Sort - Antes: ", float_nums)
print("Bucket Sort - Después: ", bucket_sort(float_nums))


# Ejemplo avanzado: ordenamiento de cadenas por longitud
def bucket_sort_strings(arr):
    if len(arr) == 0:
        return arr
    
    max_len = max(len(s) for s in arr)
    buckets = [[] for _ in range(max_len + 1)]

    for s in arr:
        buckets[len(s)].append(s)

    sorted_arr = []
    for bucket in buckets:
        # Podemos ordenar alfabéticamente dentro de cada cubo
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr

strings = ["hola", "mundo", "python", "algoritmo", "bucketSort", "a"]
print("\nStrings antes: ", strings)
print("Strings ordenados por longitud: ", bucket_sort_strings(strings))
