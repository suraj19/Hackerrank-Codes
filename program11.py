'''Joining the Sting with a different chareccter at given position'''

def mutate_string(string, position, character):
    string=list(string)
    pos=position
    ch=character
    string[pos]=ch
    return ''.join(string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
