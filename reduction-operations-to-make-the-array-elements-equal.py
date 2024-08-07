class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()  
        cnt = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] != nums[i + 1]:
                cnt += (n - (i + 1))
        
        return cnt
# space complexity = o(1)
# time complexity =o(nlogn)
