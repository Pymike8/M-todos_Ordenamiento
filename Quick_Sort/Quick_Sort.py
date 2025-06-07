def quick_sort(arr):
    _quick_sort(arr, 0, len(arr)-1)

def _quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        _quick_sort(arr, low, pi-1)
        _quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Ejemplo con números
nums = [10, 7, 8, 9, 1, 5]
print("\nQuick Sort - Antes: ", nums)
quick_sort(nums)
print("Quick sort - Después: ", nums)



#Ejemplo modificado para ordenar objetos con atributos
def quick_sort_objects(arr, key_func):
    _quick_sort_objects(arr, 0, len(arr)-1, key_func)

def _quick_sort_objects(arr, low, high, key_func):
    if low < high:
        pi = partition_objects(arr, low, high, key_func)
        _quick_sort_objects(arr, low, pi-1, key_func)
        _quick_sort_objects(arr, pi+1, high, key_func)

def partition_objects(arr, low, high, key_func):
    pivot = key_func(arr[high])
    i = low-1
    for j in range(low, high):
        if key_func(arr[j]) <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name}:{self.age}"
    def __lt__(self, other):
        return self.age <other.age
    
people = [Person("Alicia", 32), Person("Alfredo", 40), Person("Angel", 27)]
quick_sort_objects(people, lambda x: x.age)
print("\nPersonas ordenadas por edad: ", people)
quick_sort_objects(people, lambda x: x.name)
print("Personas ordenadas por nombres: ", people)
