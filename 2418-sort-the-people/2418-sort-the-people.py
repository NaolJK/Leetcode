class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        i = 1
        length = len(names)
        
        while i < length:
            
            j = i
            minimum_name = names[i]
            minimum_height = heights[i]
            while minimum_height > heights[j-1] and j>0:
                heights[j] = heights[j-1]
                names[j] = names[j-1]
                j-=1
            heights[j] = minimum_height
            names[j] = minimum_name
            i+=1
        return names
            
            
                    
        