'''
Read a given string, change the character at a given index and then print the modified string. 
'''

def mutate_string(string, position, character):

    text = string[:position] + character + string[position+1:]
    return text


''''
OTRA FORMA DE HACERLO
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
'''
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)