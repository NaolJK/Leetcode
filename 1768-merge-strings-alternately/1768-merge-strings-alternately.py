class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer_one,pointer_two = 0,0
        stack = []
        
        while pointer_one < len(word1) and pointer_two < len(word2):
            stack.append(word1[pointer_one])
            stack.append(word2[pointer_two])
            pointer_one+=1
            pointer_two+=1
        
        while pointer_one < len(word1):
            stack.append(word1[pointer_one])
            pointer_one+=1
        
        while pointer_two < len(word2):
            stack.append(word2[pointer_two])
            pointer_two+=1 
            
        
        return ("".join(stack))
            
            
        