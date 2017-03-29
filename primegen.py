"""
Peter wants to generate some prime numbers for his cryptosystem. Help him! Your
task is to generate all prime numbers between two given numbers!

Input:
The input begins with the number t of test cases in a single line (t<=10). In
each of the next t lines there are two numbers m and n (1 <= m <= n <=
1000000000, n-m<=100000) separated by a space.

2
1 10
3 5

Output:
For every test case print all prime numbers p such that m <= p <= n, one number
per line, test cases separated by an empty line.

2
3
5
7

3
5

http://www.spoj.com/problems/PRIME1/
"""
import math
import sys


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0):
            return False
    return True 


def primegen_print(primes):
    for p in primes:
        print p
    print "\n"


def primegen_range(m, n):
    """Return a list of primes in [m, n]. """
    primes = []

    if m < 4:
        if m <= 2:
            primes = [2, 3,]
        elif m == 3:
            primes = [3,]
        m = 5

    for num in xrange(m, n+1):
        if is_prime(num) is True:
            primes.append(num)

    return primes


def primegen_upto(n):
    """Return a list of primes from (2, n]. """
    primes = [2, 3,]
    for num in xrange(5, n+1, 2):
        if is_prime(num) is True:
            primes.append(num)

    return primes



def main():
    ntests = tmp = int(raw_input())
    bounds = list()

    while tmp != 0:
        a, b = raw_input().split()
        a = int(a)
        b = int(b)
        l = [a, b]
        bounds.append([a, b])
        tmp -= 1

    for l in bounds:
        p = primegen_range(l[0], l[1])
        primegen_print(p)


if __name__ == "__main__":
    main()
