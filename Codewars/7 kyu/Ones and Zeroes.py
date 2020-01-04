"""
Created on Tue Oct 29 15:37:08 2019

@author: zachp

This program will take in an array of ones and zeroes and convert the equivalent
binary value to an integer.

Eg. [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:*
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

*Note, the arrays can have varying length and are not limited to 4.
"""

def binary_array_to_number(arr):
    powers = list(range(len(arr)-1, -1, -1))
    
    final = 0
    for i in range(len(arr)):
        final += arr[i] * 2 ** powers[i]
        
    return final


assert binary_array_to_number([0,0,0,1]) == 1, 'Failed to resolve 1'
assert binary_array_to_number([0,0,1,0]) == 2, 'Failed to resolve 2'
assert binary_array_to_number([1,1,1,1]) == 15, 'Failed to resolve 15'
assert binary_array_to_number([0,1,1,0]) == 6, 'Failed to resolve 6'