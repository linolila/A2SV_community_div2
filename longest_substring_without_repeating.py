class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      uni_set = set()
      res = 0
      l = 0
      for i in range(len(s)) :
            while s[i] in uni_set:
                uni_set.remove(s[l])
                l+=1
            uni_set.add(s[i])
            res = max(res , i-l+1)
      return res
          
