'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 
'''
import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = list(s)
    print(hour)

    # Si es por la tarde
    if s.endswith('AM') == True:
        if s[:2] == '12':
            hour[0] = '0'
            hour[1] = '0'
        else:
            hour[0] = str(int(hour[0]) + 1)
            hour[1] = str(int(hour[1]) + 2)

    # Juntar cadena
    hour = ''.join(hour)

    print(hour)



    
    


if __name__ == '__main__':

    print("\nIntroduce hora: ")
    s = input()

    result = timeConversion(s)



