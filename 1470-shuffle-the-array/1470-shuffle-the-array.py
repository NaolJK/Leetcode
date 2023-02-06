class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ptr1 = 0
        ptr2 = len(nums)//2
        ans = []
        while ptr2 < len(nums):
            ans.append(nums[ptr1])
            ans.append(nums[ptr2])
            ptr1+=1
            ptr2+=1
        return ans
            
        