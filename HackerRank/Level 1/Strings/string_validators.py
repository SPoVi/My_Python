'''
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, 
alphanumeric characters, digits, etc.

str.isalnum()
    This method checks if all the characters of a string are 
    alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
    This method checks if all the characters of a string are
     alphabetical (a-z and A-Z).

str.isdigit()
    This method check if all the characters of a string are 
    digits (0-9)

str.islower()
    This method checks if all the characters of a string are
    lowecase characters (a-z)

str.isupper()
    This method checks if all the characters of a string are
    uppercase characters (A-Z)
'''

'''
TASK
You are given a string S.
Your task is to find out if the string contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters. 
'''

def checkString(s):

    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print (any(method(c) for c in s))



if __name__ == '__main__':
    print("\nIntroduce la frase: ")
    string = input()

    checkString(string)