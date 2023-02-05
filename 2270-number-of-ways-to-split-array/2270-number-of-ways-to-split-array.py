class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        tot = 0
        for i,num in enumerate(nums):
            tot+=num
            nums[i] = tot
        count = 0
        for i in range(0,len(nums)-1):
            n1 = nums[i]
            n2 = nums[-1] - n1
            if n1 >= n2:
                count+=1 
        return count
            
        
        
        