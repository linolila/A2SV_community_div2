class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
       
        cntv , res , l = 0 , 0 ,0

        for r in range(len(s)) :
            
            if s[r] in vowels :
                    cntv +=1
            if r  - l + 1 > k :
                cntv-=1 if s[l] in  vowels else 0
                l+=1
            
            res = max(res , cntv)
          
        return res
        
               
   
