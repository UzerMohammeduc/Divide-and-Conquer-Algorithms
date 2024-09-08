# Quick Sort Algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: return the array if it's already sorted
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    return quick_sort(left) + middle + quick_sort(right)  # Recursively sort

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: return if array is already sorted
    mid = len(arr) // 2  # Find the middle index
    left = merge_sort(arr[:mid])  # Recursively sort the left half
    right = merge_sort(arr[mid:])  # Recursively sort the right half
    return merge(left, right)  # Merge the sorted halves

# Function to merge two sorted arrays
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the algorithms
arr_quick = [10, 7, 8, 9, 1, 5]
sorted_quick = quick_sort(arr_quick)
print("Sorted array using Quick Sort:", sorted_quick)

arr_merge = [12, 11, 13, 5, 6, 7]
sorted_merge = merge_sort(arr_merge)
print("Sorted array using Merge Sort:", sorted_merge)
