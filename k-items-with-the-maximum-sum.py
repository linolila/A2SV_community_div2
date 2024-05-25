class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes :
            return k
        if k < numOnes + numZeros:
            return numOnes
        k -= numOnes + numZeros
        return numOnes - k
        # stor = []
        # max_sum = 0
        # if numOnes:
        #     for i in range(numOnes):
        #         stor.append(1)
        # if numZeros :
        #      for i in range(numOnes):
        #         stor.append(0)
        # else :
        #      for i in range(numNegOnes):
        #         stor.append(-1)
        
        # for i in range(k):
            
        #        max_sum += stor[i]
            
       
        # return max_sum
