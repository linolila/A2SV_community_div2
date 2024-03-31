class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        operations = 0
        to_be_removed = set()
        while l < r: 
            curr_sum = nums[l] + nums[r]
            if k == curr_sum:
                to_be_removed.add(l)
                to_be_removed.add(r)
                operations += 1
                l += 1
                r -= 1
            elif k < curr_sum:
                r -= 1
            else:
                l += 1
        for index in sorted(to_be_removed, reverse=True):
            nums.pop(index)
        return operations
