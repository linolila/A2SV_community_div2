class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        expected_sum_squares = n * (n + 1) * (2 * n + 1) // 6
        actual_sum = sum(nums)
        actual_sum_squares = sum(x * x for x in nums)
        diff_sum = expected_sum - actual_sum  
        diff_squares = expected_sum_squares - actual_sum_squares
        missing_plus_duplicate = diff_squares // diff_sum
        missing = (missing_plus_duplicate + diff_sum) // 2
        duplicate = missing - diff_sum
        
        return [duplicate, missing]
