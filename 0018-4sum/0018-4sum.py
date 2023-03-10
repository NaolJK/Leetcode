class Solution:
    def fourSum(self, nums: List[int], t: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for k in range(len(nums)-3):
            if k != 0 and nums[k] == nums[k-1]:
                continue
            
            for i in range(k+1, len(nums)-2):
                if i != k+1 and nums[i] == nums[i-1]:
                    continue

                left,right = i+1, len(nums)-1
                target =  t - (nums[i] + nums[k])
                while left < right:
        
                    if nums[left] + nums[right] > target:
                        right-=1
                    elif nums[left] + nums[right] < target:
                        left+=1
                    else:
                        ans.append((nums[k],nums[i],nums[left],nums[right]))
                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        left+=1
                        while right > left and nums[right] == nums[right-1]:
                            right-=1
                        right-=1

        return (ans)
