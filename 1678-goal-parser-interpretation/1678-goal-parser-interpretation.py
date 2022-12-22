class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        j = i+1
        stack = []
        
        while i < len(command):
            if command[i] == "(":
                if j < len(command) and command[j] != ")":
                    stack.append("al")
                    i = j+3
                    j = i+1
                else:
                    stack.append("o")
                    i = j + 1
                    j = i + 1
            else:
                stack.append("G")
                i = j
                j = i + 1
                    
        return "".join(stack)
                    
                    
        