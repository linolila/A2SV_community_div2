import math
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for i in range(len(points)):
            distance = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
            ans.append(points[i])
        ans.sort(key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
        return ans[:k]
