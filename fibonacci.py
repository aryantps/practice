def fibo(number):
    fibo_list = [1,1]
    if number > 2 :
        for i in range(2,number):
            fibo_list.append(fibo_list[i -1] + fibo_list[i - 2])
    return(fibo_list[number-1])
    
number = int(input("Enter a number : "))
print("Fibonacci number at index {} is {}".format(number, fibo(number)))
#for i in range (1,2000):
#    print(str(i) + " => " + str(fibo(i)) + "\n\n")