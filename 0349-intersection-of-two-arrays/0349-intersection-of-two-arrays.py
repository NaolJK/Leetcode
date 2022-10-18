class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_len = len(nums1)
        sec_len = len(nums2)
        
        result = []
        if first_len > sec_len:
            for i in range(sec_len):
                if nums2[i] in nums1:
                    result.append(nums2[i])
        else:
            for i in range(first_len):
                if nums1[i] in nums2:
                    result.append(nums1[i])
        
        return list(set(result))