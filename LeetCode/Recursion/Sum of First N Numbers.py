'''

Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.


Examples:
Input : N = 4

Output : 10

Explanation : first four natural numbers are 1, 2, 3, 4.

Sum is 1 + 2 + 3 + 4 => 10.

Input : N = 2

Output : 3

Explanation : first two natural numbers are 1, 2.

Sum is 1 + 2 => 3.

'''


class Solution:
    def NnumbersSum(self, N):
        # your code goes here

        if N == 0:
            return 0

        return N + self.NnumbersSum(N - 1)