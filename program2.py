'''Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''
a=int(input('Enter the Values for a: '))
b=int(input('Enter the values for b: '))
'''def sum(a,b):
    print('Sum of two Numbers: ',a+b)
def sub(a,b):
    print('Difference between two numbers: ',a-b)
def mul(a,b):
    print('Product of two numbers: ',a*b)

sum(a,b)
sub(a,b)
mul(a,b)'''
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
print('Sum of two Numbers: ',sum(a,b))
print('Difference between two numbers: ',sub(a,b))
print('Product of two numbers: ',mul(a,b))
