from math import gcd
from functools import reduce

def lcm(a,b):
    return a // gcd(a,b) * b

def get_smallest_number(n):
    return reduce(lcm,range(1 + n//2,n+1),1)




def get_smallest_number_2(n):
    """
    returns the smallest number that is divisible by numbers from 1 to n
    """
    divisors = range(1, n+1)
    check_divisible = lambda x: all([x % y == 0 for y in divisors])
    i = 1
    while True:
        if check_divisible(i):
            return i
        i += 1




def get_smallest_number_3(list1):
    lcm = list1[0]
    for i in list1[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    return lcm






print(get_smallest_number(12))
print(get_smallest_number_2(12))
print(get_smallest_number_3([1,2,3,4,5,6,7,8,9,10,11,12]))

