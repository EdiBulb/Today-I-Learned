import math
import os
import random
import re
import sys

def solve(s):
    # Split the string by spaces while retaining spaces
    words = s.split(' ')
    # Capitalize each word while preserving original spaces
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = solve(s)
    
    fptr.write(result + '\n')
    fptr.close()