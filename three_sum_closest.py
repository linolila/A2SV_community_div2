class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        minm = sum(nums[:3])
        nums.sort()
        for i in range(len(nums) - 2) :
             
            if nums[i] == nums[i-1]: continue
            l , r = i + 1 , len(nums) - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                diff  = abs(three_sum - target)
                diffr = abs(minm - target)
                if diff < diffr : 
                    minm = three_sum
                elif three_sum > target :
                    r-=1
                elif three_sum < target :
                    l+=1
                else :
                    return target
        return (minm)
