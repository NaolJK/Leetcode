class Solution:
    def decodeString(self, s: str) -> str:
        i, ans = 0, []
        
        def DecodeString():
            nonlocal i , s , ans
            
            num = []
            while i < len(s) and s[i] != "[":
                if s[i].isdigit():
                    num.append(s[i])
                    i+=1
            tims = int("".join(num))
            i+=1
            
            letters = []
            while i < len(s) and s[i] != "]":
                if s[i].isdigit():
                    res = DecodeString()
                    letters.append(res)
                else:
                    letters.append(s[i])
                    i+=1
                    
            chars = "".join(letters)
            i+=1
            
            return tims*chars
        
        while i < len(s):
            if s[i].isalpha():
                ans.append(s[i])
                i+=1
                
            else:
                result = DecodeString()
                ans.append(result)
                
        final = "".join(ans)
        return final
                    