class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        print(paths)
        for idx,path in enumerate(paths):
            if path == "":
                if len(stack) and stack[-1] == "/":
                    continue
                else:
                    stack.append("/")
            elif path == "..":
                if len(stack) >= 2:
                    stack.pop()
                    stack.pop()
                else:
                    stack.pop()
                if len(stack) == 0:
                    stack.append("/")
            elif path == ".":
                continue
            elif path != "":
                if stack[-1] != "/":
                    stack.append("/")
                stack.append(path)
                
        # print(stack)
        if len(stack) == 0 or (len(stack) ==1 and stack[0]=="/"):
            return "/"
        ans = "".join(stack)
        return ans.rstrip("/")
            
            
            
                
            
        