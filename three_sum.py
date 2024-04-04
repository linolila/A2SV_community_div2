class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue 
            l , r = i + 1 , len(nums) - 1
            
            while l < r :
                three_sum = nums[i] + nums[r]  + nums[l]
                if three_sum == 0 :
                    output.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l+=1
                    while l < r and nums[r] == nums[r - 1]:
                        r-=1
                    l+=1
                    r-=1
                elif three_sum > 0 :
                    r-=1
                else:
                    l+=1
                   
            
        return output
