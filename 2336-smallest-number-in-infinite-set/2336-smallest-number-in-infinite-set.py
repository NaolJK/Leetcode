class SmallestInfiniteSet:

    def __init__(self):
        self.added = set()
        self.nums = []
        
        heapify(self.nums)
        
        for i in range(1,1000+1):
            heappush(self.nums,i)
            self.added.add(i)
        
        

    def popSmallest(self) -> int:
        if len(self.nums):
            r = heappop(self.nums)
            # print(r, self.added)
            self.added.remove(r)
            return r
        return -1
            
        

    def addBack(self, num: int) -> None:
        if num not in self.added:
            heappush(self.nums, num)
            self.added.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)