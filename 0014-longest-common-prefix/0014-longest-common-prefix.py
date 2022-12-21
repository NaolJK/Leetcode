class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # stack = list(strs[0])
        strs = sorted(strs)
        i,j = 0,0 
        
        ans = ""
        if len(strs) == 1:
            return strs[0]
        
        
        
        while i<len(strs[0]) and j<len(strs[-1]) and strs[0][i] == strs[-1][j]:
            ans += strs[0][i]
            i+=1
            j+=1
            
        return (ans)
        
















                

                
        # print(prefix)

                    

        