class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (str(nums[i])+str(nums[j])) >= (str(nums[j]) + str(nums[i])):
                    continue
                else:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                  
        return (str(int("".join(map(str,nums)))))