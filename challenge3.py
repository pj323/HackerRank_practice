#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(string, query):
    # Write your code here
    count = 0
    result = []
    for i in range(len(query)):
        for j in range(len(string)):
            if query[i] == string[j]:
                count += 1
        result.append(count)
        count = 0
    return result
    
    
    # Write your code here


