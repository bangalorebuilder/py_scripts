from __future__ import print_function
import os
import sys


def timeConversion(s):
    if s[8:9] == 'P' or s[8:9] == 'p':
        if s[:2] == '12':
            return '12' + s[2:8]
        else:
            converted = int(s[:2]) + 12
            return str(converted) + s[2:8]
    else:
        if s[:2] == '12':
            return '00' + s[2:8]
        else:
            return s[:8]


if __name__ == '__main__':
    for i in range(9):
        result = timeConversion('0'+str(i)+':45:54PM')
        print(result)
