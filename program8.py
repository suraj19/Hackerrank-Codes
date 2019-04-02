'''You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string S.'''
def swap_case(s):
    string=s
    return string.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
