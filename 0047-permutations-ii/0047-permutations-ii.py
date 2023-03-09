class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        visited = set()
        def permutation(i):
            if i == len(nums):
                # print(nums, i)
                ans.append(tuple(nums[::]))
                return
            
            for j in range(i,len(nums)):
                if j!=i and nums[j] == nums[j-1]:
                    continue
                
                nums[i],nums[j] = nums[j],nums[i]
                permutation(i+1)
                nums[j],nums[i] = nums[i],nums[j]
                
        permutation(0)
        return list(set(ans))
        