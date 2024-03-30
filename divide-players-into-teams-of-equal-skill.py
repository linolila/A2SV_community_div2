

class Solution: 
    def dividePlayers(self, skill: List[int]) -> int:
      
        skill.sort()
        chemistry = 0
        l, r = 0, len(skill) - 1
        
        while l < r:
            team_sum = skill[l] + skill[r]
            if team_sum == skill[l+1] + skill[r-1]:
                chemistry += skill[l] * skill[r]
                r -= 1
                l += 1
            else:
                return -1
        
        return chemistry

        # n = len(skill)
        # total_skill = sum(skill)
        
        # if total_skill % (n // 2) != 0:
        #     return -1
        
        # target_skill = total_skill // (n // 2)
        
        # skill.sort()
        # left, right = 0, n - 1
        # chemistry = 0
        
        # while left < right:
        #     if skill[left] + skill[right] != target_skill:
        #         return -1
        #     chemistry += skill[left] * skill[right]
        #     left += 1
        #     right -= 1
        
        # return chemistry
