class Solution:
    def candy(self, ratings: List[int]) -> int:
        toright = [1]*len(ratings)
        toleft = [1]*len(ratings)
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                toright[i]+=(toright[i-1])
    
        for j in range(len(ratings)-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                toleft[j]+=(toleft[j+1])
        
        total=0
        k = 0
        while k < len(ratings):
            res = max(toleft[k], toright[k])
            total+=res
            k+=1
        
        return total
            
            
        