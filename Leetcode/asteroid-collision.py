class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for num in asteroids:

            while num < 0 and stack and stack[-1] > 0 and stack[-1] < (-1*num):
                stack.pop()
            
            if num < 0 and stack and stack[-1] == (-1*num):
                stack.pop()
                continue

            if num < 0 and stack and stack[-1] > 0:
                continue

            stack.append(num)

            # print(stack)
# 
        return stack


        