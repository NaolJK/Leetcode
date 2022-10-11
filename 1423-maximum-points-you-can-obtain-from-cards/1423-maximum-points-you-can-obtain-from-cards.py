class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length_of_all = len(cardPoints)
        length_of_window = length_of_all - k
        all_sum = sum(cardPoints)
        
        left_window = 0
        right_window = 0
        minimum = res = sum(cardPoints[:length_of_window])
        
        left_window = 0
        right_window = length_of_window -1
        
        while right_window+1 < length_of_all:
            right_window+=1
            res-= cardPoints[left_window]
            res+= cardPoints[right_window]
            minimum = min(res, minimum)
            left_window+=1
            
        
        return all_sum - minimum
        
            
            
            
        
        
        
        
                
            
            
            
                
            
        