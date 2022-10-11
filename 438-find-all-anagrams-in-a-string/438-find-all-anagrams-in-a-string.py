class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
    
        result = []
        frequency = Counter(p)
        length_of_dist = len(frequency)

        left_window,right_window = 0,0
        length_of_sub = len(p)

        while(right_window < len(s)):
            if s[right_window] in frequency:
                frequency[s[right_window]] -= 1
                if(frequency[s[right_window]] == 0): length_of_dist -= 1
            if(right_window - left_window + 1 < length_of_sub): 
                right_window += 1
            else:
                if(length_of_dist == 0): 
                    result.append(left_window)

                
                if s[left_window] in frequency: 
                    frequency[s[left_window]] += 1
                    
                    if(frequency[s[left_window]] == 1): 
                        length_of_dist += 1
    
                left_window += 1
                right_window += 1

        return result
                
            
        