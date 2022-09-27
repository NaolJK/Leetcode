class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = dict(Counter(nums))
        count=0
        print(result)
        for i in result:
            if((k - i in result) and (result[k-i] > 0)):
                count += min(result[i], result[k-i])
        return count//2        