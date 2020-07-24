# TO-DO: complete the helper function below to merge 2 sorted arrays
#Python 3 Version
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []
    # Your code here
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    if a < len(arrA):
        merged_arr.extend(arrA[a:])
    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr



# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2 : ])
        arr =  merge(left, right)

    return arr
import time

t = time.clock()
arrA = [1, 3, 44, 5, 6, 9, 39, 24]
print(merge_sort(arrA))
z = time.clock()
print(z-t)


#Python 2.7 Version
# def merge(arrA, arrB):
#     # num_elements = len(arrA) + len(arrB)
#     merged_arr = []
#     a_idx, b_idx = 0, 0
#     while a_idx < len(arrA) and b_idx < len(arrB):
#         if arrA[a_idx] < arrB[b_idx]:
#             merged_arr.append(arrA[a_idx])
#             a_idx += 1
#         else:
#             merged_arr.append(arrB[b_idx])
#             b_idx += 1
#     if a_idx == len(arrA):
#         merged_arr.extend(arrB[b_idx:])
#     else:
#         merged_arr.extend(arrA[a_idx:])
#     return merged_arr

# TO-DO: implement the Merge Sort function below recursively
# Python 2.7 Version
# def merge_sort(arr):
#     # Your code here
#     if len(arr) <= 1:
#         return arr
#     l, r = merge_sort(arr[:len(arr)/2]), merge_sort(arr[len(arr)/2:])
#
#     return merge(l, r)


    # return arr

# c = [1, 4, 2, 6, 3]
# d = [22, 23, 21, 9]
# print(merge(c,d))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
#
# import random
# a = []
# b = []
# for i in range(1, 20):
#     n = random.randint(1, 30)
#     a.append(n)
#     b.append(n)

# c = [1, 4, 2, 6, 3]
# d = [22, 23, 21, 9]
#
# print(merge_sort(c))
