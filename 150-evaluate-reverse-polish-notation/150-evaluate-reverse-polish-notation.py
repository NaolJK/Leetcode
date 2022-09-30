
            


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        operators = {
            '+': lambda x,y:x+y,
            '-': lambda x,y:x-y,
            '*': lambda x,y:x*y,
            '/': lambda x,y:x/y
        }

        for token in tokens:
            if token in operators:
                second, first = stack.pop(), stack.pop()
                stack.append(int(operators[token](first, second)))
            else:
                stack.append(int(token))
        
        return stack[0]         
                
        