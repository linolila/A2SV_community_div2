class Solution:
    def minSteps(self, n: int) -> int:
            if n == 1:
               return 0
            dp = [float('inf')] * (n + 1)
            dp[1] = 0 
            for i in range(2, n + 1):
                for j in range(1, int(i**0.5) + 1):
                    if i % j == 0:
                        factor1, factor2 = j, i // j
                        dp[i] = min(dp[i], dp[factor1] + factor2)
                        dp[i] = min(dp[i], dp[factor2] + factor1)
            
            return dp[n]
