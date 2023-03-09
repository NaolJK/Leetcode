class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans =[]
        def backtrack(num, path):
            if num > n+1:
                return
            
            if len(path) == k:
                ans.append(path[::])
                return
            
            path.append(num)
            backtrack(num+1,path)
            path.pop()
            backtrack(num+1,path)

        path = []
        backtrack(1,path)
        return ans