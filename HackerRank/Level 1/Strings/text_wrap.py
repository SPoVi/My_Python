'''
You are given a string and width .
Your task is to wrap the string into a paragraph of width . 
'''

import textwrap

def wrap(string, max_width):
    len_s = len(string)
    my_string = []

    counter = 0
    for l in range(len_s):
        
        if counter != 0 and counter % max_width == 0:
            my_string.append('\n')

        my_string.append(string[l])
        #print("\nMy cadena:\n {}".format(my_string))
        counter += 1
    
    my_string = ''.join(my_string)
    #print("\nMy cadena: {}".format(my_string))
            

            
    return my_string

if __name__ == '__main__':
    print("\nIntroduce string y separacion: ")
    string, max_width = input(), int(input())
    #string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    #max_width = 4
    result = wrap(string, max_width)
    print("\nMy cadena:\n{}".format(result))