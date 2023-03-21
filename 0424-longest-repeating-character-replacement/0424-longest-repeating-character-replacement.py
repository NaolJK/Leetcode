class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = [0]*26
        left = 0
        window = 0
        for right in range(len(s)):
            idx = ord(s[right]) - 65
            letters[idx]+=1
            while sum(letters)- max(letters) > k:
                idx = ord(s[left])-65
                letters[idx]-=1
                left+=1
            window = max(right-left+1, window)
                
        return (window)
            
        