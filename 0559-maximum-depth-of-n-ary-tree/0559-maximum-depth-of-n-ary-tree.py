"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        count = 0
        stack = [root]
        while stack:
            children = []
            while stack:
                node = stack.pop()
                if node.children:
                    children.extend(node.children)
                    
            stack = children
            count+=1
        return count 
                
        
        
                
        