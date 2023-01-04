class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        answer = []
        pointer = 0
        idx = 0
        while idx < len(s):
            if pointer < len(spaces) and idx == spaces[pointer]:
                pointer+=1
                answer.append(" ")
            answer.append(s[idx])
            idx+=1
        
        answer = "".join(answer)
            
        return (answer)
                
        
            
        
            