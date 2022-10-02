class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        while i < k:
            inserted = nums.pop()
            nums.insert(0,inserted)
            i+=1