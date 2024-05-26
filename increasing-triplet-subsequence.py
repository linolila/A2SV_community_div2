class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        min_num = float('inf')
        second_min_num = float('inf')
        
        for num in nums:
            if num <= min_num:
                min_num = num
            elif num <= second_min_num:
                second_min_num = num
            else:
                return True
        
        return False
