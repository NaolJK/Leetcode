class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        
        all_length = len(s)
        
        left_window = 0
        # right_window = 0
        max_count = 0
        v =0
        
        for right_window in range (all_length):
            if s[right_window] in vowels:
                v+=1
            if (right_window - left_window+1) == k:
                max_count = max(max_count, v)
                if s[left_window] in vowels:
                    v-=1
                    
                left_window+=1
                
        return (max_count)
                
            
            
        
        
        
        