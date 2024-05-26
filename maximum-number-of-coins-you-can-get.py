class Solution:
    def maxCoins(self, piles: List[int]) -> int:
      
        piles.sort()
        j = 0
        n = len(piles)
        coins = 0
        for i in range(n - 2, 0, -2):
            coins += piles[i]
            j += 1
            if j == n // 3:
                return coins
        return coins
