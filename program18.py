'''There is an array of n integers. There are also  disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i∈A, you add 1 to your happiness. If i∈B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements.
However, the array might contain duplicate elements.


Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.'''
n,m=map(int,input().split())
array=(input().split())
A=set(input().split())
B=set(input().split())
count=0
#print(A)
#print(B)
#print(sum([(i in A) - (i in B) for i in array]))
for i in array:
    if i in A:
        count+=1
    elif i in B:
        count-=1
print(count)
