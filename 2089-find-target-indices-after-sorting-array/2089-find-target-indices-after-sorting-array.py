class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if target not in nums:
            return []
        ans = []
        for idx,num in enumerate(nums):
            if target == num:
                ans.append(idx)
        return ans
        