class StockSpanner:

    def __init__(self):
        self.values =[]

    def next(self, price: int) -> int:
        count = 1
        while self.values and self.values[-1][0] <= price:
            num,freq = self.values.pop()
            count+=freq
        
        self.values.append((price, count))
        return count
            
            
            
                
                
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)