class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        cur_sum = 0
        min_leng = maxsize
        for i in range(len(nums)):
            cur_sum += nums[i]

            while cur_sum >= target :
                min_leng = min(min_leng , i - l + 1)
                cur_sum -= nums[l]
                l+=1
                

        
        
        
        
        return min_leng if min_leng != maxsize else 0
