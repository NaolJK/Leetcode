class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        visited = set()
        def permutation(candidate):
            
            if len(candidate) == len(nums):
                ans.append(candidate[::])
                return 
            
            for i in range(0,len(nums)):
                if i not in visited:
                    candidate.append(nums[i])
                    visited.add(i)
                    permutation(candidate)
                    candidate.pop()
                    visited.remove(i)
                
        permutation([])
        return ans
                