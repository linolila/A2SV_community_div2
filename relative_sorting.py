class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
       remaining = []
       res = []
       for num in arr2:
          res.extend([num] * arr1.count(num))
       for num in arr1:
           if num not in arr2 :
                 remaining.append(num)
       res.extend(sorted(remaining))
       return(res)
