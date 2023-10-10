class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        
        sz_hay = len(haystack)
        
        sz_nee = len(needle)

        p = 26
        
        m = 10 ** 9 + 9
        
        ascii_a = ord('a')
        
        pow = [0] * max(sz_hay, sz_nee)
        
        
        
        sz_pow = len(pow)

        pow[0] = 1
        
        for i in range(1,sz_pow):
            
            pow[i] = (pow[i-1] * p) % m
            
        # print(pow)
        
        hash = [0] * (sz_hay+1)

        for i in range(sz_hay):
            
            hash[i+1] = (hash[i] + (ord(haystack[i]) - ascii_a + 1) * pow[i]) % m
            
        
        hash_needle = 0

        for i in range(sz_nee):
            
            hash_needle = (hash_needle + (ord(needle[i]) - ascii_a + 1) * pow[i]) % m
            # print(hash_needle)
        
        stat = -1

        for i in range(sz_hay - sz_nee + 1):
            
            cur_hash = (hash[i+sz_nee] + m - hash[i]) % m
            
            if (hash_needle * pow[i]) % m == cur_hash:
                
                stat = i
                
                break

        return stat