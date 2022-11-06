class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        
        for num in nums:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
                
        index = 0
        
        for j in range(0,len(nums),2):
            nums[j] = even[index]
            nums[j+1] = odd[index]
            
            index+=1
            
        
        return nums
        
        
            
            
        
                