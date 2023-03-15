class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            res = bin(i)[2:]
            ans.append(res.count("1"))
        return ans