def binary_search(arr,number):
    first = 0
    last = len(arr) - 1
    flag = 0
    while first < last :
        mid = (first + last ) //2
        if number == arr[mid]:
            flag = 1
            break
        elif number > arr[mid]:
            first = mid + 1
        elif number < arr[mid]:
            last = mid 
    return flag
        
#driver code
arr = []  # 2,4,9,15,35
n = int(input("Input no. of elements in array:  ",))
for i in range(0,n):
    arr.append(int(input("Enter {} value : ".format(i+1))))

number = int(input("\nInput no which has to be searched : "))


if binary_search(arr,number) == 0:
    print("\n{} can not be found in array".format(number))
    print("\nSEARCH UNSUCCESSFUL")
else:
    print("\n{} is in the list :)".format(number))
    print("\nSEARCH SUCCESSFUL")