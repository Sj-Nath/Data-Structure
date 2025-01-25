fac_list = [None] *100

def factorial(n):

    if n == 0 or n ==1 :
        return 1
    
    while fac_list[n] == None:
        fac_list[n] = n * factorial(n-1)

    return fac_list[n]

print(factorial(5))