class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        last_smaller = 0
        res = 0
        for idx,num in enumerate(arr):
            
            while stack and stack[-1][1] >= num:
                index, value = stack.pop()
                if len(stack):
                    left_count = index - stack[-1][0] - 1
                    right_count = idx - index - 1 
                else:
                    left_count = index
                    right_count = idx - index - 1
                ans = (value*left_count) + (value*right_count)+value*(left_count*right_count)
                # print(value,left_count, right_count,ans)
                res+=ans
            stack.append((idx,num))
        
        while stack:
            index, value = stack.pop()
            right_count = len(arr) - index - 1
            if len(stack):
                left_count = index - stack[-1][0] - 1 
            else:
                left_count = index
            ans = (value*left_count) + (value*right_count) + value*(left_count*right_count)
            # print(value,left_count, right_count,ans)
            res+=ans
            
        return (res + sum(arr))%(10**9 + 7)
            
                
                    
            
                
                
                
                
                