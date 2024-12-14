import time
problemSize = 10000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
 start = time.time()
 # Algorithm logic (dummy example)
 work = 0
 for x in range(problemSize):
 work += 1
 end = time.time()
 elapsed = end - start
 print("%12d%16.3f" % (problemSize, elapsed))
 problemSize *= 2

sorted dataset (length = 1000).
def linear_search(arr, target):
 for i in range(len(arr)):
 if arr[i] == target:
 return i
 return -1
def binary_search(arr, target):
 low = 0
 high = len(arr) - 1
 while low <= high:
 mid = (low + high) // 2
 if arr[mid] == target:
 return mid
 elif arr[mid] < target:
 low = mid + 1
 else:
 high = mid - 1
 return -1

def bubble_sort(arr):
 n = len(arr)
 for i in range(n):
 for j in range(0, n-i-1):
 if arr[j] > arr[j+1]:
 arr[j], arr[j+1] = arr[j+1], arr[j]
def insertion_sort(arr):
 for i in range(1, len(arr)):
 key = arr[i]
 j = i-1
 while j >= 0 and key < arr[j]:
 arr[j+1] = arr[j]
 j -= 1
 arr[j+1] = key
def selection_sort(arr):
 for i in range(len(arr)):
 min_idx = i
 for j in range(i+1, len(arr)):
 if arr[j] < arr[min_idx]:
 min_idx = j
 arr[i], arr[min_idx] = arr[min_idx], arr[i]