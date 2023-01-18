class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        i = 0
        length = len(nums)
        while i < length:
            num = str(nums[i])
            nums.append(int(num[::-1]))
            i+=1
     
        return len(set(nums))
            
                