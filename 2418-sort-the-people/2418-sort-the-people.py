class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            for j in range(i, len(names)):
                if heights[i] < heights[j]:
                    temp = heights[i]
                    temp2 = names[i]
                    heights[i] = heights[j]
                    names[i] = names[j]
                    heights[j] = temp
                    names[j] = temp2
        return (names)
                    
        