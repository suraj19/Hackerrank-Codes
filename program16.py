'''The first line contains the integer,N, the total number of plants.
The second line contains the N space separated heights of the plants.'''
def average(array):
    # your code goes here
    unique_array=set(array)
    return sum(unique_array)/len(unique_array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
