class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def Invert(n, k):
            if n == 1:
                return "0"
            
            #call n recursively till it reaches s0
            ans = Invert(n-1, k)

            #when i reaches s0 reverse the coming string from s(n-1) invert it and append it to one
            final = ""
            for a in ans:
                if a == "1":
                    final+="0"
                else:
                    final+="1"
                    
            #finally do s(n-1) + "1" + reverse of inverted string then return it to f(n+1)
            ans  = ans + "1" + final[::-1]
            return ans
        
        
        final_ans = Invert(n, k)
        return final_ans[k-1]
