'''Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.'''
M=int(input())
arr1=set(map(int, input().split()))
N=int(input())
arr2=set(map(int, input().split()))
#print(M.difference(N)==N.difference(M))
new1=arr1.difference(arr2)
new2=arr2.difference(arr1)
new1.update(new2)
#print(sorted(new1))
symmetric=sorted(new1)
for i in symmetric:
    print(i)
