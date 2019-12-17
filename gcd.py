# gcd using loops
def computeGCD(num1, num2):
    if num1 > num2:
        small = num2
    else: 
        small = num1
    for i in range(1, small+1):
        if(num1%i==0) and (num2%i==0):
            gcd = i
    return gcd

# gcd of two numbers using Euclidean algorithm
def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1%num2
    return num1

# gcd of list of numbers
def gcd(lst: list):
    gcd = find_gcd(lst[0], lst[1])
    for elem in range(2, len(lst)):
        gcd = find_gcd(gcd, lst[elem])
    return gcd
