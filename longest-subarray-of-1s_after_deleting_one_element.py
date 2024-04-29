class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        res = 0
        zeros = 0
        for i in range(len(nums)) :
            zeros+=1 if nums[i] == 0 else 0
            while zeros > 1:
                zeros -=1 if nums[l] == 0 else 0 
                l+=1
            res = max(res , i - l)
        return res
