class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        ptr1 = 0
        ptr2 = len(piles)-1
        ptr3 = ptr2 - 1
        total = 0
        
        while ptr3 > ptr1:
            total+=piles[ptr3]
            ptr1+=1
            ptr2-=2
            ptr3-=2
        return (total)
            
        