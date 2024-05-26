class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        rearranged = [1] 
        for i in range(1, len(arr)):
           
            rearranged.append(min(arr[i], rearranged[-1] + 1))
        
        return max(rearranged)
