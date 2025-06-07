def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Ejemplo con una lista grande
import random
big_list = [random.randint(1, 1000) for _ in range(100)]
print("\nLista grande antes: ", big_list[:10], "...")
merge_sort(big_list)
print("Lista grande después: ", big_list[:10], "...")


# Ejemplo con objetos complejos (por atributo)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"{self.name}:{self.age}"
    def __lt__(self, other):
        return self.age <other.age
    
people = [Person("Alicia", 32), Person("Alfredo", 40), Person("Angel", 27)]
print("\nPersonas antes: ", people)
merge_sort(people)
print("Personas después: ", people)
