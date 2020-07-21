# TO-DO: complete the helper function below to merge 2 sorted arrays
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

#Python 3 Version
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []

    merged_arr.append(arrA) + merged_arr.append(arrB)
    # Your code here
​
​
    return merged_arr

c = [1, 4, 2, 6, 3]
d = [22, 23, 21, 9]
print(merge(c,d))
​
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
​
​
    return arr



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
