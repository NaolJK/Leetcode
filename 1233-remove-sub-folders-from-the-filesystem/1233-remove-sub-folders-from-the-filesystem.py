class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        folder.sort(key=lambda x: len(x))
        
        seen = set()
        
        final = []

        for x in folder:
            
            for i in range(2, len(x.split('/'))):
                
                if tuple(x.split('/')[1:i]) in seen:
                    
                    break
            else:
                
                final.append(x)
                
                seen.add(tuple(x.split('/')[1:]))
        
        return final