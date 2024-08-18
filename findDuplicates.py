class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        duplicates = [num for num, cnt in count.items() if cnt == 2]
        
        return duplicates
        duplicates = []

    # i = 0
    # while i < len(nums):
    #     correct_index = nums[i] - 1
    #     if nums[i] != nums[correct_index]:
    #         # Swap nums[i] with nums[correct_index]
    #         nums[i], nums[correct_index] = nums[correct_index], nums[i]
    #     else:
    #         if i != correct_index and nums[i] != nums[nums[i] - 1]:
    #             duplicates.append(nums[i])
    #         i += 1

    # return duplicates


