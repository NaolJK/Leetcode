
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        deliciousness.sort()
        mod = (10**9) + 7
        n = 0
        res = 0
        power = []
        count = 0
        freq = dict(Counter(deliciousness))
        
        while res < 2**21:
            res = 2**n
            n+=1
            power.append(res)
        
        print(power)
        print(freq)
        for key,amount in freq.items():
            # print(key, end=" ")
            if (key + key) in power and amount > 1: 
                summation = (amount * (amount-1))//2
                count+=summation
            
            for p in power:
                value = p - key
                if value in freq and value != key and key > value:
                    summation = amount * freq[value]
                    count += summation

        
        return count % mod
            
        
            
            
            
            
        
    
        
        
    
    
        
        