class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        def compare(x, y):
           return 1 if x + y > y + x else -1
        nums.sort(key=cmp_to_key(compare), reverse=True)
        result = "".join(nums)
        return "0" if result[0] == "0" else result
