class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict(Counter(nums))
        # print(frequency)
        frequency_sorted = sorted(frequency.items(), key= lambda x:x[1],reverse=True)
        # print(frequency_sorted)
        highest_keys = [x[0] for x in frequency_sorted]
        
        
        return highest_keys[:k]