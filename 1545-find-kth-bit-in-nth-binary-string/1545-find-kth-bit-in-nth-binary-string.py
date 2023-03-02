class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def Invert(n, k):
            if n == 1:
                return "0"

            ans = Invert(n-1, k)
            final = ""
            for a in ans:
                if a == "1":
                    final+="0"
                else:
                    final+="1"

            ans  = ans + "1" + final[::-1]
            return ans
        return Invert(n, k)[k-1]
