from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
            max_or = 0
            for num in nums:
                max_or |= num
            def count_subsets_with_max_or():
                total_count = 0
                n = len(nums)
                for i in range(1, 1 << n): 
                    subset_or = 0
                    for j in range(n):
                        if i & (1 << j):  
                            subset_or |= nums[j]
                    if subset_or == max_or:
                        total_count += 1
                
                return total_count
            return count_subsets_with_max_or()
