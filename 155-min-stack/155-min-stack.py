class MinStack:

    def __init__(self):
        self.min_stack = []
        self.size = 0
        

    def push(self, val: int) -> None:
        self.min_stack.insert(0,val)
        self.size+=1
        

    def pop(self) -> None:
        self.size -= 1
        self.min_stack.remove(self.min_stack[0])
        

    def top(self) -> int:
        return self.min_stack[0]
        

    def getMin(self) -> int:
        return min(self.min_stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()