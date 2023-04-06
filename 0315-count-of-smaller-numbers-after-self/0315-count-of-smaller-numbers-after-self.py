class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)
        
        def mergeSort(arr):
            
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            
            left = arr[:mid]
            right = arr[mid:]
            
            left_arr = mergeSort(left)
            right_arr = mergeSort(right)
            
            p1, p2 = 0, 0
            
            while p1 < len(left_arr) and  p2 < len(right_arr):
                if left_arr[p1][1] > right_arr[p2][1]:
                    p2+=1
                else:
                    # print("1st here",left_arr[p1],left_arr,right_arr,p2)
                    count[left_arr[p1][0]]+=p2
                    p1+=1
                
            
    
                    
            while p1 < len(left_arr):
                # print("here",left_arr[p1],left_arr,right_arr,p2)
                count[left_arr[p1][0]] += p2
                p1+=1
                
            # print(left_arr,right_arr, count, p2,p1)
            
            l, r , merged = 0,0,[]
            
            while l < len(left_arr) and r < len(right):
                if left_arr[l][1] < right_arr[r][1]:
                    merged.append(left_arr[l])
                    l+=1
                else: 
                    merged.append(right_arr[r])
                    r+=1
            
            while l < len(left_arr):
                merged.append(left_arr[l])
                l+=1
            
            
            while r < len(right_arr):
                merged.append(right_arr[r])
                r+=1
                
            return merged
        
        for i,n in enumerate(nums):
            nums[i] = (i, n)
            
        mergeSort(nums)
        
        for i , n in nums:
            nums[i] = count[i]
            
        return nums
            
        
                    
                    
            