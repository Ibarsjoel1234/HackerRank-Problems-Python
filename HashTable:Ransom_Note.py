#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    return (Counter(note) - Counter(magazine)) == {}.      # Counter is used to create dictonary 

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    a = checkMagazine(magazine, note)
    
    if a:
        print("Yes")
    else:
        print("No")

Explaination:
   Checking the word in magazine and note.
   It is easy way to substract them.
   if note is substracted with magazine and it return to empty dictonary then we can find that the note had contained same word what magazine has.
