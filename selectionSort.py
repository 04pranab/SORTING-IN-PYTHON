import random

# Random list generation of size n:
def Gen_Ran_List(n=random.randint(10, 100), low=random.randint(1, 50), up=random.randint(51, 100)):
    lt = list(set([random.randint(low, up) for i in range(n)]))
    random.shuffle(lt)
    return lt


def SelectionSort(arr):
    for i in range(len(arr)):
        tab = i
        for j in range(i+1, len(arr)):
            if arr[tab] > arr[j]:
                tab = j
        if tab != i:
            arr[i], arr[tab] = arr[tab], arr[i]
    return arr

lt = Gen_Ran_List()
length = len(lt)
print(f"A random list of length {length} is created. And the list has: \n {lt}")
lt1 = SelectionSort(lt)
print(f"After SelectionSort: \n {lt1}")