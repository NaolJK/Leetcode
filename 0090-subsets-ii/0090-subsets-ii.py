class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        nums.sort()
        
        def sub(i,candidate):
            
           
            ans.add(tuple(candidate[::]))
            
            for j in range(i,len(nums)):
                candidate.append(nums[j])
                sub(j+1,candidate)
                candidate.pop()
                
                
        sub(0,[])
        return list(ans) 