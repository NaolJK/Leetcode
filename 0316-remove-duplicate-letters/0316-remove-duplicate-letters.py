class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        indexs ={}
        stack = []
        
        for idx,string in enumerate(s):
            indexs[string] = idx
        
        for i,string in enumerate(s):
            if string in stack:
                continue
            
            while stack and stack[-1] > string and indexs[stack[-1]] > i:
                stack.pop()
            stack.append(string)
            
        return "".join(stack)
        
        
        