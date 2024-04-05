class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort()
        secondList.sort()
        res = []
        l, r = 0, 0

        while l < len(firstList) and r < len(secondList):
            minm = max(firstList[l][0], secondList[r][0])
            maxm = min(firstList[l][1], secondList[r][1])

            if minm <= maxm:
                res.append([minm, maxm])

            if firstList[l][1] < secondList[r][1]:
                l += 1
            else:
                r += 1

        return res
