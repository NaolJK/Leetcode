class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if num1[0] == '0' or num2[0] == '0':
            return "0"
        
        num1_len = len(num1)
        num2_len = len(num2)
        ans_length = (num1_len + num2_len)
        ans = [0] * (ans_length)
        
        position_to_insert = len(ans) - 1
        
        for i in range(num2_len-1,-1,-1):
            running_pointer = position_to_insert
            for j in range(num1_len-1,-1,-1):
                result = int(num2[i]) * int(num1[j])
                mul_carry = int(result / 10)
                ones = result % 10
                added_res = int(ans[running_pointer]) + int(ones) 
                added_ones = added_res % 10
                added_carry = int(added_res / 10)
                carries = added_carry + mul_carry
                ans[running_pointer] = str(added_ones)
                ans[running_pointer - 1] = str(carries + int(ans[running_pointer-1]))
                # print(ans) 
                running_pointer-=1           
            position_to_insert-=1
            
        
         
        final = "".join(ans)
        
        if ans[0] == '0':
            # ans.pop(0)
            
            return (final[1:])
        
        return final
        
       
      
        
            
                
                
            
        
        
        