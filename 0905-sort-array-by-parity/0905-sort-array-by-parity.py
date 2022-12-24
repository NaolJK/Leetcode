class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sorted_res = []
        for num in nums:
            if num % 2 == 0:
                sorted_res.insert(0,num)
            else:
                sorted_res.append(num)
        return sorted_res