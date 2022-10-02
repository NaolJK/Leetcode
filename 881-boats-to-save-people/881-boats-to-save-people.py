class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        length = len(people) -1
        i = 0 
        j = length
        count = 0
        
        while i <= j:
            if people[i] + people[j] <= limit:
                count +=1
                i+=1 
                j-=1
            else:
                j-=1
                count+=1
        return count
                
                
                
                
                
        