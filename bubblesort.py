def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#driver code
arr = []  # 2,4,9,15,35
n = int(input("Input no. of elements in array:  ",))
for i in range(0,n):
    arr.append(int(input("Enter {} value of list : ".format(i+1))))

bubblesort(arr)

print("\nSorted array is:  ",str(arr)[1 : -1])
