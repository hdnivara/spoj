"""
Adding reversed numbers.

http://www.spoj.com/problems/ADDREV/

Input:
The input consists of N cases (equal to about 10000). The first line of the
input contains only positive integer N. Then follow the cases. Each case
consists of exactly one line with two positive integers separated by space.
These are the reversed numbers you are to add.

3
24 1
4358 754
305 794

Output:
For each case, print exactly one line containing only one integer - the
reversed sum of two reversed numbers. Omit any leading zeros in the output.

34
1998
1
"""

def reverse(n):
    new = 0
    while n > 0:
        r = n % 10
        new = r + (new * 10)
        n = n // 10

    return new


def parse_input():
    pairs = list()
    ntests = tmp = int(raw_input())

    while tmp != 0:
        a, b = raw_input().split()
        pairs.append([long(a), long(b)])
        tmp -= 1

    return pairs


def main():
    inputs = parse_input()

    for nums in inputs:
        a = reverse(nums[0])
        b = reverse(nums[1])
        print reverse(a + b)


if __name__ == "__main__":
    main()

