class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:  
        stack = []
        result = [0]*len(temperatures)
        # final = []
        
        for i in range(len(temperatures)):
            count = 1
            
            while stack and stack[-1][0] < temperatures[i]:
                ans = stack.pop()
                diff = i-ans[1]
                result[ans[1]] = diff     
            
            stack.append([temperatures[i],i])
        
        print(result)
        print(stack)
            
        return (result)
        
        
        
                
            
        
                
                
        