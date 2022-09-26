class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort();
        res = []
        left = 0
        right = len(nums) - 1
        while(len(nums) != len(res)):
            res.append(nums[left])
            left+=1
            
            if(left <= right):
                res.append(nums[right])
                right-=1
                
        return res