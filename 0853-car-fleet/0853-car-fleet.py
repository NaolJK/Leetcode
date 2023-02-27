class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = (zip(*sorted(zip(position, speed))))
        time = [((target-position[i])/speed[i]) for i in range(len(speed))]
        
        stack = []
        for t in time:
            while len(stack) and stack[-1] <= t:
                stack.pop()
            stack.append(t)
            
        return len(stack)
        
        