class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)

        def atmost(goal):
            
            left = cnt = 0
            
            for right in range(len(str_num)):


                while left <= right and (right - left + 1 > goal):
                    left+=1
                    
                sm = int(str_num[left:right+1])
                
                if sm != 0 and num != 0 and num % sm == 0 and right - left + 1 == goal:
                   
                    cnt+=1
                    
            return cnt 
        
        ans = atmost(k)
                
        return ans 
        