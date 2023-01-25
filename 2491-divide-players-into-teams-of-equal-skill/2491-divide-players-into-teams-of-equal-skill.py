class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        start, end = 0, len(skill)-1
        last_sum = 0
        ans = 0
        while start < end:
            total = skill[end] + skill[start]
            if last_sum == 0:
                last_sum = total
                ans = skill[end] * skill[start]
            else:
                if total != last_sum:
                    return -1
                mul = skill[end] * skill[start]
                ans+=mul
            start+=1
            end-=1
        return (ans)
            
                    
            
        