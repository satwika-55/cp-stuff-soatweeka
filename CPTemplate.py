 ########        #        #########   #       #  #######  #     #        #
#       #       # #           #       #       #     #     #    #        # # 
#              #   #          #       #       #     #     #  #         #   #  
 #######      #######         #       #   #   #     #     ##          #######     
        #    #       #        #       #   #   #     #     #  #       #       #
#       #   #         #       #       #  # #  #     #     #    #    #         #  
########   #           #      #       ##    ##    ######  #      # #           #  

# JAI MAHAKAAL

# RADHE RADHE

import os
import sys
import time
import random
import re
import math
import threading
import bisect
#sys.stdin = open('inout.txt', 'r')
#sys.stdout = open('output.txt', 'w')

#the above 2 statements are to be used only for VS Code while running the test cases

# Collections and Data Structures
from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, permutations
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce

# gives list of primes upto 'limit' numbers
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# Constants
MOD1 = int(1e9 + 7)
MOD2 = 998244353
INF = int(1e17)
inf = float('inf')

# Alphabet and Vowel Lists
alphabets = list("abcdefghijklmnopqrstuvwxyz")
vowels = list("aeiou")

# Input Functions
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))



