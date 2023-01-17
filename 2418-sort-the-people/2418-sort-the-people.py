class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            minimum = i
            
            for j in range(i,len(heights)):
                if heights[j] > heights[minimum]:
                    minimum = j
                
            heights[i],heights[minimum] = heights[minimum],heights[i]
            names[i],names[minimum] = names[minimum],names[i]
            
        return names
        
                    
        