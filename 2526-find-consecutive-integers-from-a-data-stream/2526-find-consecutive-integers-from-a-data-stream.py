class DataStream:
    
    def __init__(self, value: int, k: int):
        self.key = k
        self.val = value
        self.count = 0

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.count+=1
        else:
            self.count = 0

        if self.count >= self.key:
            return True
        return False
            

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/