"""
Trailing zeros in factorial of a number.

http://www.spoj.com/problems/FCTRL/

For example, they defined the function Z. For any positive integer N, Z(N) is
the number of zeros at the end of the decimal form of number N!. They noticed
that this function never decreases. If we have two numbers N1<N2, then Z(N1) <=
Z(N2). It is because we can never "lose" any trailing zero by multiplying by
any positive number. We can only get new and new zeros. The function Z is very
interesting, so we need a computer program that can determine its value
efficiently.

Input:
There is a single positive integer T on the first line of input (equal to about
100000). It stands for the number of numbers to follow. Then there are T lines,
each containing exactly one positive integer number N, 1 <= N <= 1000000000.

Output:
For every number N, output a single line containing the single non-negative
integer Z(N).
"""

def trailing_zeros(n):
    """ Return the number of trailing zeros in a given number.

    Factorials can tend to be very large numbers, but it's easy to count the
    trailing zeros without computing the actual factorial.

    Traling zero is added whenever a number is multiplied by 10 (or mulitples
    of 10). 10 has factors (5, 2). So, just by computing the numbers that are
    divisible by 5 (and it's powers), we can compute the trailing zeros.

    Eg., 45600 --> 2, 3342 --> 0 and so on.
    """

    i = 1
    zeros = 0

    while True:
        rem = int(n / (5 ** i))

        if rem >= 1:
            zeros += int(rem)
            i += 1
        else:
            break

    return zeros


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
        print trailing_zeros(n)


if __name__ == "__main__":
    main()
