class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def permutation(i,nums):
            if i >= len(nums):
                ans.append((nums[::]))
                return
            
            for j in range(i,len(nums)):
                if j>i and nums[i] == nums[j]:
                    continue
                
                nums[i],nums[j] = nums[j],nums[i]
                permutation(i+1,nums[::])
                # nums[j],nums[i] = nums[i],nums[j]
                
        permutation(0,nums)
        return (ans)
        