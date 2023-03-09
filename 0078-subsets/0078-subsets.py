class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def sub(i,candidate):
            
           
            ans.append(candidate[::])
            
            for j in range(i,len(nums)):
                candidate.append(nums[j])
                sub(j+1,candidate)
                candidate.pop()
                
                
        sub(0,[])
        return ans 
        