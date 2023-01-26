class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(final):
            start = 0 
            while start < final:
                arr[start], arr[final] = arr[final],arr[start]
                start +=1
                final-=1
                
        length = len(arr)-1
        result = []
        for i in range(length, -1,-1):
            max_num = i 
            # print(i)
            
            for j in range(i, -1, -1):
                # print(j)
                if arr[j] > arr[max_num]:
                    max_num = j
                    print(j)
            
            if max_num != i:
                # print(max_num)
                flip(max_num)
                flip(i)
                result.append(max_num+1)
                result.append(i+1)
                    
        return result
        