class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dist_nums_1 = [value for value in nums1 if value not in nums2]
        dist_nums_2 = [value for value in nums2 if value not in nums1]
        
        return [list(set(dist_nums_1)), list(set(dist_nums_2))]
        