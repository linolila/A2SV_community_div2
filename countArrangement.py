class Solution:
    def countArrangement(self, n: int) -> int:
        
   
            def backtrack(position):
                if position > n:
                    return 1
                
                count = 0
                for num in range(1, n + 1):
                    if not used[num]:
                        if (position % num == 0) or (num % position == 0):
                            used[num] = True
                            count += backtrack(position + 1)
                            used[num] = False
                
                return count
            used = [False] * (n + 1)
            return backtrack(1)

       
      
         
