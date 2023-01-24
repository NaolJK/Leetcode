class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        ptr1 = 0
        ptr2 = len(piles)- 2
        total = 0
        
        while ptr2 > ptr1:
            total+=piles[ptr2]
            ptr1+=1
            ptr2-=2
        return (total)
            
        