class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabets = ["a","b","c","d","e","f","g","h","i"
                     ,"j","k","l","m","n","o","p",
                     "q","r","s","t","u","v","w","x","y","z"]
        
        ans = ""
        i = len(s) - 1 
        while i >= 0:
            if s[i] == "#":
                digit = s[i-2] + s[i-1]
                ans+=alphabets[int(digit)-1]
                i-=2
            else:
                idx = int(s[i])
                ans+=alphabets[idx-1]
                print(s[i])
            i-=1
        
        return (ans[::-1])
    
            
            
            
        
        