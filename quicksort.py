import random

def QuickSort(arr):
    if len(arr) <= 1:  
        return arr
    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    
    return QuickSort(left) + [pivot] + QuickSort(right)

# Random list generation of size n:
def Gen_Ran_List(n=random.randint(10, 100), low=random.randint(1, 50), up=random.randint(51, 100)):
    lt = list(set([random.randint(low, up) for i in range(n)]))
    random.shuffle(lt)
    return lt

lt = Gen_Ran_List()
length = len(lt)
print(f"A random list of length {length} is created. And the list has: \n {lt}")
lt1 = QuickSort(lt)
print(f"After QuickSort: \n {lt1}")
