
from typing import List

class Solution:
    def isPossible(self, N: int, coins: List[int]) -> bool:
        sum_val = sum(coins)
        isSum = [[False] * (sum_val + 1) for _ in range(N + 1)]
        
        for i in range(N + 1):
            isSum[i][0] = True
        
        for i in range(1, sum_val + 1):
            isSum[0][i] = False
        
        for i in range(1, N + 1):
            for j in range(1, sum_val + 1):
                if j < coins[i - 1]:
                    isSum[i][j] = isSum[i - 1][j]
                if j >= coins[i - 1]:
                    isSum[i][j] = isSum[i - 1][j] or isSum[i - 1][j - coins[i - 1]]
        
        for i in range(1, sum_val + 1):
            if (i % 20 == 0 or i % 24 == 0 or i == 2024) and isSum[N][i]:
                return True
        
        return False
        


