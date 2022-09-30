class Solution:
    def reverseParentheses(self, s: str) -> str:
        letter_stack = []
        result = ""
        for character in s:
            if character == "(":
                # print(result)
                letter_stack.append(result)
                result = ""
            elif character == ")":
                result = result[::-1]
                result = letter_stack.pop() + result
            else:
                result+=character
        return result
                
                
        
        