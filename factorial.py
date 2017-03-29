"""
Small factorials

Calculate factorials of some small positive integers.

http://www.spoj.com/problems/FCTRL2/

Input:
An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines,
each containing a single integer n, 1<=n<=100.

4
1
2
5
3

Output:
For each integer n given at input, display a line with the value of n!

1
2
120
6
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


def parse_input():
    nums = list()
    ntests = tmp = int(raw_input())

    while tmp != 0:
        nums.append(long(raw_input()))
        tmp -= 1

    return nums


def main():
    inputs = parse_input()
    for n in inputs:
        print factorial(n)


if __name__ == "__main__":
    main()
