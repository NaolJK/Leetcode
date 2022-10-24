class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        all_list = [i for i in range(1,n+1)]
        
        index = 0
        
        def winnerRec(index,k):
            if len(all_list) == 1:
                return all_list[0]
            index = (index + k-1) % len(all_list)
            del all_list[index]
            
            return winnerRec(index,k)
        
        return winnerRec(index,k)
            
        
        