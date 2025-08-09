'''
def add(x,y):
    return(x+y)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The sum is:", add(a,b))
'''
# factorial using function
'''
def fact(n):
    if  n == 1:
        return 1
    return n * fact(n-1)
n=int(input())
print(fact(n))    
'''
'''
def add(n):
    if n<=1:
        return n
    return n + add(n-1)
print(add(int(input())))
'''
# Fibonacci series using recursion
'''
def fibb(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return fibb(n-1) + fibb(n-2)
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibb(i))
    '''
# sets
'''
a=2
set_a = {1,2,3,4,5}
print(type(set_a))
print(set_a)
'''

# dictionary
'''
dict_a = {'name': 'Niyaz', 'age': 20, 'city': 'Bangalore'}
print(type(dict_a))
print(dict_a)
'''