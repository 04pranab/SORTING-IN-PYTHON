import random

# Random list generation of size n:
def Gen_Ran_List(n=random.randint(10, 100), low=random.randint(1, 50), up=random.randint(51, 100)):
    lt = list(set([random.randint(low, up) for i in range(n)]))
    random.shuffle(lt)
    return lt

# Insertion Sort Implementation
def InsertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
lt = Gen_Ran_List()
length = len(lt)
print(f"A random list of length {length} is created. And the list has: \n{lt}")
lt1 = InsertionSort(lt)
print(f"After InsertionSort: \n{lt1}")
