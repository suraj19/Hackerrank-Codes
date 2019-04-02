'''Task
Read two integers and print two lines. The first line should contain integer division, a//b .
The second line should contain float division,  a/b .

You don't need to perform any rounding or formatting operations.'''
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
def floor(a,b):
    return a//b
def div(a,b):
    return a/b
print(floor(a,b))
print(div(a,b))
