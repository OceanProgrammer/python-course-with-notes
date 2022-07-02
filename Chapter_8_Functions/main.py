# n = int(input())
# print(n+2)

# def new_func():
#     i=0
#     while i<10:
#         i+=1
#         print(i)

# new_func()

def product():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Product is: ", a*b)

def division(a,b=6):
    """This function returns the division of 2 numbers."""
    return a/b

# product()
division(12,6) #Function call 
# 12-a, 6-b; a/b(12/6)->2.0

n = division(12, 2) #3.0
# print(n)
# print(division.__doc__)

def sum(n): #1+2+3+4+5
    sum = 0
    for i in range(n):
        i = (i+1)
        sum = sum + i
    print(sum)

# sum(6)

def sum_recursive(n):
    if n==0:
        return 0
    return n + sum_recursive(n-1)

print(sum_recursive(5))

"""
sum_r(5)
-> 5+ sum_r(4)
->5 + 4+sum_r(3)
-> 5+4+3+sum_r(2)
->5+4+3+2+sum_r(1)
->5+4+3+2+1+sum_r(0)
->5+4+3+2+1+0 = 15
"""

"""
(1+2+3+4+5)
-> 1+ (2+3+4+5)
"""