'''You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.

Input Format

The first line contains a string, S.
The second line contains the width, W.'''

import textwrap
def text_wrap(string,width):
    return textwrap.fill(string, width)
stin='hwegfiuwgwkbIwifwifbwifhwfwibfsIB'
width=4
print(text_wrap(stin,width))
