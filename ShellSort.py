import random

# Random list generation of size n:
def Gen_Ran_List(n=random.randint(10, 100), low=random.randint(1, 50), up=random.randint(51, 100)):
    lt = list(set([random.randint(low, up) for i in range(n)]))
    random.shuffle(lt)
    return lt

# Insertion Sort Implementation
def ShellSort(arr, gap):
    if gap == 0:
        return arr

    n = len(arr)
    
    for i in range(gap, n):
        temp = arr[i]
        j = i
        while j >= gap and arr[j - gap] > temp:
            arr[j] = arr[j - gap]
            j -= gap
        arr[j] = temp

    # Recursive call with reduced gap
    return ShellSort(arr, gap // 2)

lt = Gen_Ran_List()
length = len(lt)
print(f"A random list of length {length} is created. And the list has: \n{lt}")
lt1 = ShellSort(lt, len(lt)//2)
print(f"After InsertionSort: \n{lt1}")
