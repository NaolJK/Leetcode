from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        
        container = SortedList()
        
        result = 0
        mod = 10**9 + 7
        
        for num in instructions:
            result += min(container.bisect_left(num), len(container) - container.bisect_right(num))
            container.add(num)
            
        return result % mod
            
        