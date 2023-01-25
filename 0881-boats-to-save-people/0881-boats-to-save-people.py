class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        start = 0 
        end = len(people) - 1
        count = 0
        
        while start <= end:
            weight = people[end] + people[start]
            if weight <= limit:
                count+=1
                start+=1
                end-=1
            else:
                count+=1
                end-=1
        return count
    
        