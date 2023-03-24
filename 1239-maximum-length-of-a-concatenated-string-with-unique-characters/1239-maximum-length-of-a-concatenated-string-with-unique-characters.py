class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        def backtrack(i=0, path=set()):
            
            self.ans = max(self.ans,len(path))
            
            for j in range(i, len(arr)):
                res = path.intersection(set(arr[j]))
                string = set(arr[j])
                
                if not res and len(string) == len(arr[j]):
                    path.update(string)
                    backtrack(j+1, path)
                    for s in string:
                        path.remove(s)
        backtrack()
        return self.ans
                
                
                    
                    
                    
                
                
          
            
        
        
        