# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        queue1 = deque([p])
        queue2 = deque([q])
        
        while queue1 and queue2:
            n1 = queue1.popleft()
            n2 = queue2.popleft()
            
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                if n1.right and n2.right:
                    queue1.append(n1.right)
                    queue2.append(n2.right)
                
                if n1.left and n2.left:
                    queue1.append(n1.left)
                    queue2.append(n2.left)
                    
                if n1.left and not n2.left:
                    return False
                if n2.left and not n1.left:
                    return False
                if n2.right and not n1.right:
                    return False
                if n1.right and not n2.right:
                    return False
        return True
        