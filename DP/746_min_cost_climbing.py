class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Two variables to track the minimum cost to reach the last two steps
        prev2 = 0 
        prev1 = 0  

        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
            
            prev2 = prev1
            prev1 = curr

        return prev1


x = Solution()
test1 = [10, 15, 20]
test2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(x.minCostClimbingStairs(test1))  
print(x.minCostClimbingStairs(test2))  
