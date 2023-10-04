class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for c in s:
        
            if not stack:
                stack.append((c, 0))
                continue
            
            if stack:
                if stack[-1][0] == c:
                    stack.append((c, 1 + stack[-1][1]))
                else:
                    stack.append((c, 0))
            
            i = 0
            check = stack and stack[-1][0] == c and stack[-1][1] == k-1
            while check and i < k:
                stack.pop()
                i+=1
        
        ans = ""
        for s in stack:
            ans+=s[0]
        return ans
                    
            
        