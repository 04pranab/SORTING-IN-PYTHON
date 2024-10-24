import random

# Random list generation of size n:
def Gen_Ran_List(n=random.randint(10, 100), low=random.randint(1, 50), up=random.randint(51, 100)):
    lt = list(set([random.randint(low, up) for i in range(n)]))
    random.shuffle(lt)
    return lt

# Merge function to combine two sorted halves
def merge(left, right):
    
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

# Merge Sort Implementation
def MergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = MergeSort(arr[:mid])   
    right = MergeSort(arr[mid:])  

    return merge(left, right)

lt = Gen_Ran_List()
length = len(lt)
print(f"A random list of length {length} is created. And the list has: \n{lt}")
lt1 = MergeSort(lt)
print(f"After MergeSort: \n{lt1}")
