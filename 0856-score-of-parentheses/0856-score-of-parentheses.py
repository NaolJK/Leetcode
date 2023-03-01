class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #initialize stack
        stack = []
        #initialize a count or res variable
        ans, i, length = 0,0, len(s)
        
        #loop till all the string is visited
        while i < length:
            #if the string is "(" append to the stack with its value by default its 0
            if s[i] == "(":
                stack.append(["(",0])
            #else
            else:
                elem,count = stack.pop()
               #check if the count of the current popped element is zero
                #if zero add one to the count of the top of stack
                if count == 0:
                    if stack:
                        stack[-1][1]+=1
                    else:
                        ans+=1
                #else
                #multiply it by two and update the top of the stack
                else:
                    value = 2*count
                    if stack:
                        stack[-1][1]+=value
                    else:
                        ans+=(value)
            i+=1
        return ans
                    
                    
                    
                    
            
                        
                    
                        
                        
                    
                    
                
            
        