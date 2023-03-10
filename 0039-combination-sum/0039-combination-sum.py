class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.total_sm = 0
        ans = []
        def backtrack(i,total_sum,path):
            if total_sum > target:
                return 
            
            if total_sum == target:
                ans.append(path[::])
                return 
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                total_sum+=candidates[j]
                backtrack(j,total_sum,path)
                path.pop()
                total_sum-=candidates[j]
                
        backtrack(0,0,[])
        return (ans)
                
            
            
                
                
            
            
        