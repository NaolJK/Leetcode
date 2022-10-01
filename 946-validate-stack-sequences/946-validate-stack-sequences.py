class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0 
        length = len(pushed)
        check_stack = []
        for elem in pushed:
            check_stack.append(elem)
            
            while len(check_stack) > 0 and (check_stack[len(check_stack)-1] == popped[i]):
                check_stack.pop()
                i+=1
                
        
        return i == length
            
                
        