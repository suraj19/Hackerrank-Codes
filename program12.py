'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.'''
def count_substring(string, sub_string):
    s=string
    sub=sub_string
    sub_len=len(sub)
    result=0
    sub_len = len(sub)
    for i in range(len(s)):
        if s[i:i+sub_len] == sub:
            result+= 1
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
