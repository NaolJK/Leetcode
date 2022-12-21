class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = list(strs[0])
        strs = sorted(strs)
        
        for s in strs:
            i = 0
            pre_pointer = 0
            # print(s)
            while i < len(s) and pre_pointer < len(stack):
                # print(s)
                if s[i] == stack[pre_pointer]:
                    pre_pointer+=1
                    # print(s[i],end=" ")
                    i+=1
                    continue
                else:
                    break
            stack = stack[0:pre_pointer]
        ans = "".join(stack)
        return (ans)
                



















                

                
        # print(prefix)

                    

        