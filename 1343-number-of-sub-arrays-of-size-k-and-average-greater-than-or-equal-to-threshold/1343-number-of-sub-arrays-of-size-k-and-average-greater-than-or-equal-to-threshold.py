class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        length_of_all = len(arr)
        left_window = 0
        count = 0
        right_window = k -1
        first_sum = sum(arr[:k])
        # print(first_sum)
        average = first_sum / k
        
        
        
        while right_window < length_of_all:
            # print(average)
            if average >= threshold:
                count+=1
            
            
            
            first_sum -= arr[left_window]
            left_window+=1
            right_window+=1
            if right_window < length_of_all:
                
                first_sum += arr[right_window]
            
            average = first_sum / k
            
        
        return (count)
            
            
                
            
            
            
        