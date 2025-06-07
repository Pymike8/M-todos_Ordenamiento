def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


# Ejemplo con listas de numeros
nums = [12, 5, 8, 9, 4]
print("Antes: ", nums)
print("Después: ", insertion_sort(nums))


# Ejmplo con lista de strings
words = ["apple", "windows", "manzana", "ventana"]
print ("\nAntes: ", words)
print("Después: ", insertion_sort(words))
