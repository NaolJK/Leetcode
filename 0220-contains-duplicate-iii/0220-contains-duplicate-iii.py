class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        size = t + 1
        hashmap = {}
        for i, num in enumerate(nums):
            idx = num // size
            # print(num,size,idx)
            if idx in hashmap:
                return True
            l,r = idx-1,idx+1
            print(num,l,r,idx)
            if l in hashmap and abs(hashmap[l]-num) <= t:
                return True
            if r in hashmap and abs(hashmap[r]-num) <= t:
                return True
            hashmap[idx] = num
            
            if len(hashmap)>k:
                hashmap.pop(nums[i-k]//size)
            
        return False