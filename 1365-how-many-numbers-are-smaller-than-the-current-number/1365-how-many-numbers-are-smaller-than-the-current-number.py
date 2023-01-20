class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = list(nums)
        sorted_list.sort()
        i = 0 
        length = len(nums)
        
        while  i < length:
            nums[i] = (sorted_list.index(nums[i]))
            i+=1
            
        return (nums)
            
        
        