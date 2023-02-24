class Solution:
    def smallestSubsequence(self, s: str) -> str:
        indexs, stack = {},[]
        
        for i,c in enumerate(s):
            indexs[c] = i
        
        for i, c in enumerate(s):
            if c not in stack:
                while len(stack) and stack[-1] > c and indexs[stack[-1]] > i:
                    stack.pop()
                stack.append(c)
            
        return("".join(stack))
        
        