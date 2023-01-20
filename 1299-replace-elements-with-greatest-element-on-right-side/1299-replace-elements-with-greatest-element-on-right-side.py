class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = arr[-1]
        length = len(arr) - 1
        i = length
        
        while i >= 0:
            if i == length:
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = maximum
                maximum = max(temp, maximum)
            i-=1
        return (arr)

                
            
        
        