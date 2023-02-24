class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for expression in tokens:
            if expression == "+" or expression == "-" or expression == "/" or expression == "*":
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                
                operation = f"{n2} {expression} {n1}"
                result = eval(operation)
                # print(operation,result)
                stack.append(str(int(result)))
            else:
                stack.append(expression)
                
        return (int(stack[0]))
                
        