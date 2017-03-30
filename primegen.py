"""
Generate all prime numbers between any two given numbers.

http://www.spoj.com/problems/PRIME1/

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


def primegen_range_sieve(m, n):
    """Generate primes in [m, n] using sieve. """
    all_primes = primegen_upto_sieve(n)

    next_prime = next(x[0] for x in enumerate(all_primes) if x[1] >= m)
    primes = all_primes[next_prime:]

    return primes


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


def primegen_upto_sieve(n):
    """Generate primes upto n using sieve. """
    limit = n + 1
    non_prime = [False] * limit
    primes = []

    for index in xrange(2, limit):
        if non_prime[index]:
            continue

        for i in xrange(index*2, limit, index):
            non_prime[i] = True

        primes.append(index)

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
        p = primegen_range_sieve(l[0], l[1])
        primegen_print(p)


def ad_main():
    ntests = 4
    bounds = [[1, 10], [3, 5], [2, 33], [17, 29]]

    for l in bounds:
        p = primegen_range_sieve(l[0], l[1])
        print l, p


if __name__ == "__main__":
    main()
    #ad_main()
