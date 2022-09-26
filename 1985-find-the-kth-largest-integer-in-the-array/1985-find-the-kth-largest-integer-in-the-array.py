class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        res = [int(i) for i in nums]
        res.sort(reverse =True)
        return str(res[k-1])