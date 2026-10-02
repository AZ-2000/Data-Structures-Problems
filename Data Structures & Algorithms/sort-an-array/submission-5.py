def Left(i):
    return ((2 * i)+1)
def Right(i):
    return ((2*i) + 2)
def Parent(i):
    return (i-1)//2

def Max_Heapify(arr, i, heap_size):
    l = Left(i)
    r = Right(i)
    if l < heap_size and arr[l] >= arr[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and arr[r] >= arr[largest]:
        largest = r
    if largest != i:
        tmp = arr[i]
        arr[i] = arr[largest]
        arr[largest] = tmp
        Max_Heapify(arr, largest, heap_size)

def Build_Max_Heap(arr, heap_size):
    for i in range((len(arr)//2)-1, -1,-1):
        Max_Heapify(arr, i, heap_size)

def HeapSort(arr):
    heap_size = len(arr)
    Build_Max_Heap(arr, heap_size)
    for i in range(len(arr)-1,0,-1):
        tmp = arr[0]
        arr[0]= arr[i]
        arr[i] = tmp
        heap_size -= 1
        Max_Heapify(arr,0, heap_size)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        HeapSort(nums)
        return nums

        