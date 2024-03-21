class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        
        for i in range(len(ranges)):
             start = ranges[i][0]
             end = ranges[i][1]
             if start <= left and left <= end:
                left = end + 1
        
        return left > right
