class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
    
        x = 1
        
        answer = []
        
        
        for i in range(len(l)):
            
            new_arr = nums[l[i]:(r[i]+1)]
            new_arr.sort()
            difference = new_arr[1] - new_arr[0]
            left = 0
            length = len(new_arr)
            
            while left < length-1:
                
                if new_arr[left+1] - new_arr[left] == difference:
                    x += 1
                    left += 1
                    
                else: 
                    x = x
                    left += 1
                    
            answer.append(bool(x == length))
            x = 1
            
        return answer