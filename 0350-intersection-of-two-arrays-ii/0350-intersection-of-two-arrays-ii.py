class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length_one = len(nums1)
        length_two = len(nums2)
        
        result = []
        
        if length_one > length_two:
            for i in range (length_two):
                if nums2[i] in nums1:
                    nums1.remove(nums2[i])
                    result.append(nums2[i])
        else:
            for i in range (length_one):
                if nums1[i] in nums2:
                    result.append(nums1[i])
                    nums2.remove(nums1[i])
        return (result)
        
        