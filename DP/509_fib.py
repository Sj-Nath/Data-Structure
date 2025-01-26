class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        prev2, prev1 = 0, 1

        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1


x = Solution()
print(x.fib(int(input())))





