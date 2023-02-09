class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        tot = 0
        for i,num in enumerate(nums):
            tot+=num
            self.nums[i] = tot
        self.nums.insert(0,0)
        

    def sumRange(self, left: int, right: int) -> int:
        ans = self.nums[right+1] - self.nums[left]
        return ans
        
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)