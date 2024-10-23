import random

# Random list generation of size n:
def Gen_Ran_List(n=random.randint(10, 100), low=random.randint(1, 50), up=random.randint(51, 100)):
    lt = list(set([random.randint(low, up) for i in range(n)]))
    random.shuffle(lt)
    return lt


def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

lt = Gen_Ran_List()
length = len(lt)
print(f"A random list of length {length} is created. And the list has: \n {lt}")
lt1 = BubbleSort(lt)
print(f"After SelectionSort: \n {lt1}")