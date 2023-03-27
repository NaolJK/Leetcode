class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        diff_arr = []
        
        for i in range(len(nums1)):
            res = nums1[i] - nums2[i]
            diff_arr.append(res)
            
        self.count = 0
            
        def mergeSort(arr):
            
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            
            left_arr = mergeSort(left_half)
            right_arr = mergeSort(right_half)
            
            p1 , p2, result = len(left_arr) - 1, len(right_arr)-1, 0
            
            while p1 >= 0 and p2 >= 0:
                right_eq = right_arr[p2] + diff
                left_eq = left_arr[p1]
                
                if right_eq >= left_eq:
                    p2-=1
                    result+=1
                else:
                    p1-=1
                    if p1 >= 0:
                        result+=(len(right_arr) - p2 - 1)
            
            
            p1-=1       
            while p1 >= 0:
                result+=(len(right_arr) - p2 - 1)
                p1-=1
            
            
            self.count+=result
            
            
            l, r, merged = 0 , 0, []
            
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] >= right_arr[r]:
                    merged.append(right_arr[r])
                    r+=1
                else:
                    merged.append(left_arr[l])
                    l+=1
            
            while l < len(left_arr):
                merged.append(left_arr[l])
                l+=1
            
            
            while r < len(right_arr):
                merged.append(right_arr[r])
                r+=1
            
            
            return merged
        
        mergeSort(diff_arr)
        
        return self.count
                    
                
                
            
            
            
            