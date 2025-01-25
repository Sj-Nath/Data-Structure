global  fib_list 
fib_list = [None for i in range(15)]
def fib(n):
    print(fib_list)
    fib_list[0] = 0
    fib_list[1] = fib_list[2] =1
    while fib_list[n] == None:
        fib_list[n] = fib(n-1) + fib(n-2)

    return fib_list[n]

print(fib(7))





