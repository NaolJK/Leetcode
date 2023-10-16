class NumArray:
    
    def RSB(self, i):
        return i & -i
    

    def __init__(self, nums: List[int]):
        
        self.length = len(nums) + 1
        self.nums = [0, *nums]
        self.tree = [0]*self.length
        
        for i in range(1, self.length):
            self.tree[i] = self.nums[i]
        
        for child in range(1, self.length):
            parent = child + self.RSB(child)
            
            if parent < self.length:
                self.tree[parent] += self.tree[child]
        

    def update(self, index: int, val: int) -> None:
        
        index += 1
        add = val - self.nums[index]
        
        self.nums[index] = val
        
        i = index
        
        while i < self.length:
            self.tree[i]+=add
            i += self.RSB(i)
        
        
    def prefix(self, i):
        ans = 0
        while i != 0:
            # print(i, self.tree)
            ans += self.tree[i]
            i-=self.RSB(i)
        
        return ans
        
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefix(right + 1) - self.prefix(left)
        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)