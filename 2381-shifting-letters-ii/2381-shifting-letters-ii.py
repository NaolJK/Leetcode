class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        string = list(s)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
                   ,'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        prefix = [0]*(len(s)+1)
        for left, right, direction in shifts:
            if direction == 1:
                prefix[left]+=1
                prefix[right+1]-=1
            else:
                prefix[left]-=1
                prefix[right+1]+=1
        prefix = list(accumulate(prefix))
        ans = []
        for i in range(len(prefix)-1):
            res = ((ord(s[i])-97)+prefix[i])%26
            ans.append(letters[res])
        return ("".join(ans))
            
            
            
                
            
            
            
            