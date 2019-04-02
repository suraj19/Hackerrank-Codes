'''Read an integer .

Without using any string methods, try to print the following:
123...N
Note that "..." represents the values in between'''
'''n=int(input('Enter the Value: ')) #using string methods
start=1
ans=''
for i in range(start,n+1):
    ans+=str(i)
print(ans)'''
n=int(input('Enter the Value: '))
for i in range(1,n+1):
    print(i,sep='',end='')
