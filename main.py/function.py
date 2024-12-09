# function
"""
def find_max(li):       # li = list
    if len(li) == 0:
        return None
    max_item = li[0]
    for item in li:
        if item > max_item:
            max_item = item

    return max_item

prices = [2,6,8,9,7,12,19,82,43,]
print(find_max(prices))
"""
"""
def find_item(li , y):  # local variable
    y = 12                # variable pathale copy hoy
    li[0] = 1            #list pathale copy hoyna
    for item in li:
        if y == item:
            return True
    print( "couldn't find",y)
    return False
prices = [2,6,8,9,7,17,19,82,43,]
x = 14
print(find_item( prices, x))
print(x)
print(prices)
"""

# Positonal argument

"""
def my_func(a,b,c):
    result = a * 3 + b * 2 + c
    return result
a,b,c = 10,20,30
r= my_func(a,b,c)
print(r)
"""

# keyword argument
"""
def my_func(a,b,c):
    result = a * 3 + b * 2 + c
    return result
#a,b,c = 10,20,30
r= my_func(a=20,b=30,c=10)
print(r)
"""
# Defult argument
"""
def my_func(a,b,c=0):
    result = a * 3 + b * 2 + c
    return result
#a,b,c = 10,20,30
r= my_func(a=10,b=20)
print(r)
"""
# Recursion function                      # Recursion limit python defult = 1000
                                          #2 type = 1. get recursion limit  2.set recursion limit
"""                                         
def print_n(n):
    if n == 0 :
        return

    print_n(n - 1)
    print(n)
print_n(9)

"""

# Recursion

"""
def print_x(x):
    print(x)
    print_x(x)

print_x(10)
"""
# GCD(a , 0) -> a
# GCD(a , b) = (b , a%b)
"""
def euclid_gcd(a , b):
    if b == 0:                # base condition
        return a
    return euclid_gcd(b, a%b)

gcd = euclid_gcd(35,90)
print(gcd)
"""

# Akata function ar vitore ar akta function

"""
def fuc(n1, n2):
    print("Received", n1, n2)

    def is_even(n):
        if n % 2 == 0:                  # kono kiso return na kore by defult None return hoy
            return True
        return False

    print(n1, is_even(n1))
    print(n2, is_even(n2))
    
#fuc(10,9)
#print(is_even(5))
f = fuc
print(f (10,9) )
"""
# value pass
"""
def fnc():
    return 1, 2, 3
                         # value kom ba beshe hole fnc kaj korba na
a, b, c= fnc()
print(a, b, c)
"""
# jodi jana na thake amra ki receive korte chace

def fuc( *args, **kwargs):
    print(args)
    print(kwargs)

fuc(3,5,9 ,a=6 ,b=10 )