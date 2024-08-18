from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_nums = set(range(1, n + 1))
        actual_nums = set(nums)
        missing_nums = list(expected_nums - actual_nums)
        
        return missing_nums
