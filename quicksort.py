def partition(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high + 1):
                if arr[j] <= pivot:
                        arr[i], arr[j] = arr[j], arr[i]
                        i = i + 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

def quicksort(arr,low,high):
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


#driver code
arr = []  # 2,4,9,15,35
n = int(input("Input no. of elements in array:  ",))
for i in range(0,n):
    arr.append(int(input("Enter {} value of list : ".format(i+1))))

quicksort(arr, 0, len(arr) - 1)

print("\nSorted array is:  ",str(arr)[1 : -1])
