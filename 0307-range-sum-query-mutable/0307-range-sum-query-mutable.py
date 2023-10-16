class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        
        self.tree = [0]*(self. n + 1)
        
        for i, num in enumerate(nums):
            self.updateTree(i+1, num)
        
    
    def updateTree(self, i , val):
        while i <= self.n:
            self.tree[i]+=val
            i+=(i & -i)
        
    def getSum(self, i):
        ans = 0
        
        while i > 0:
            ans += self.tree[i]
            i -= (i & -i)
        return ans

    def update(self, index: int, val: int) -> None:
        
        diff = val - self.nums[index]
        
        self.nums[index] = val
        
        self.updateTree(index + 1, diff)
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.getSum(right+1) - self.getSum(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)