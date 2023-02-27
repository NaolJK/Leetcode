class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_sec = 0
        queue = deque(tickets)
        
        while queue[k] != 0:
            for i in range(len(tickets)):
                if queue[i] != 0:
                    queue[i]-=1
                    time_sec+=1 
                    
                if i == k and queue[i] == 0:
                    return time_sec
        
                
                
            
            
            
       
            
        