import re
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        ans = []
        for path in paths:
            splitted_path = path.split()
            start = splitted_path[0]
            for idx in range (1,len(splitted_path)):
                content = splitted_path[idx].split("(")
                file_content = content[1][:-1]
                path = start+"/"+content[0]
                
                if file_content not in files:
                    files[file_content] = [path]
                else:
                    files[file_content].append(path)
                    
        for key,values in files.items():
            if len(values) > 1:
                ans.append(values)
        return ans
            