class Solution:
    def compress(self, chars: List[str]) -> int:
        left,right = 0, 0
        ans = []
        while right < len(chars):
            while right < len(chars) and chars[left] == chars[right]:
                right+=1
            
            count = right - left
            if count <= 1:
                ans+=chars[left]
            else:
                c = list(str(count))
                ans+=chars[left]
                ans.extend(c)
                
            left = right
            
        chars.clear()
        chars.extend(ans)
        return len(chars)
        
       
                
            
        
        