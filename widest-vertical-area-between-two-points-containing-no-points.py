class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxm = 0
        for i in range(len(points) -1) :
           maxm = max(maxm,points[i+1][0] - points[i][0])
        return maxm
         
