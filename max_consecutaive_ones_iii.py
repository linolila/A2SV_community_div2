class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        res = 0
        zeros = 0
        for i in range(len(nums)) :
           if nums[i] == 0 :
              zeros+=1
           
           while zeros > k:
             if nums[l] == 0 :
                zeros-=1
             l+=1
           res = max(res , i - l + 1)
        return res
