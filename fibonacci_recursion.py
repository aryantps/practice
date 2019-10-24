def fibo(number):
    if (number == 1 or number == 2):
        return 1
    else:
        return fibo(number - 1) + fibo(number - 2)

number = int(input("Enter a number : "))
print("Fibonacci number at index {} is {}".format(number, fibo(number)))