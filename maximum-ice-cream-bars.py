class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        if costs [0] > coins :
            return 0
        for i in range(len(costs)) :
            
            if coins != 0  and costs[i] <= coins:
                coins = coins - costs[i]
                cnt  += 1
        return cnt
        # time complexity = o(nlogn)
        # space complexity = o(1)
