from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        count_map = defaultdict(int)
        
        for num in nums1 :
            count_map[num] +=1
        
        for num in nums2 :
            if num in count_map and count_map[num] > 0 :
                intersection.append(num)
                count_map[num] -=1
        return intersection
