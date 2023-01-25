class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height)-1
        left = 0
        maximum = 0
        while left < right:
            width = right - left
            length = min(height[left], height[right])
            area = width * length
            maximum = max(maximum,area)
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return maximum
            
            