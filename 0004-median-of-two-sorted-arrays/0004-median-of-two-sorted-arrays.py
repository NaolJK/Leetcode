class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr = []
        
        p1 = p2 = 0
        
        while p1 < len(nums1) and p2 < len(nums2):
            
            if nums1[p1] > nums2[p2]:
                arr.append(nums2[p2])
                p2+=1
            
            else:
                arr.append(nums1[p1])
                p1+=1
        
        while p1 < len(nums1):
            arr.append(nums1[p1])
            p1+=1
            
        while p2 < len(nums2):
            arr.append(nums2[p2])
            p2+=1
            
        n  = len(arr)
        
        if n % 2:
            # print(arr)
            return arr[n//2]
        else:
            
            return (arr[n//2] + arr[(n//2) - 1 ]) / 2
        
        