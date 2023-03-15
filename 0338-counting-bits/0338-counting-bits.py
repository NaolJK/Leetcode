class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        temp = dict()
        
        def dp(i):
            if i == 0:
                return 0
            if i in temp:
                return temp[i]
            res = dp(i//2)
            dp(i - 1)
            if i & 1:
                res+=1
            temp[i] = res
            ans.append(res)
            return res
        dp(n)
        return (ans)
            