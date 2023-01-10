class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        stack = [0]*len(boxes)
        for idx,box in enumerate(boxes):
            for b_idx,ball in enumerate(boxes):
                if ball == "1":
                    stack[idx]+=abs(idx - b_idx)
        
        return (stack)
            
            