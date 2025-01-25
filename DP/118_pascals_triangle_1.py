class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        dp = []
        
        for r in range(numRows):
            row = [1] * (r + 1)
            for c in range(1, r):
                row[c] = dp[r-1][c-1] + dp[r-1][c]
            dp.append(row)
        
        return dp
x = Solution()
print("\n".join([str(i) for i in x.generate(25)]))

        