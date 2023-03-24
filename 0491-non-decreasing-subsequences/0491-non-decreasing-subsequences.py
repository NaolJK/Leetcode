class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        
        def backtrack(i, path):
            
            if len(path) >= 2 and tuple(path) not in ans:
                ans.add(tuple(path[::]))
                
            for j in range(i, len(nums)):
                if (not len(path) or path[-1] <= nums[j]):
                    path.append(nums[j])
                    backtrack(j+1,path)
                    path.pop()
            return 
        backtrack(0,[])
        return list(ans)
            
        
        