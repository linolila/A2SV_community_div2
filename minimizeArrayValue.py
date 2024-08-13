class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = tot = nums[0]
        for i in range(1,len(nums)) :
            tot += nums[i]
            result = max(result , math.ceil(tot / (i + 1)))
        return result

