# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0 

        def dC(node,currentD):
           
            if not node:
                self.maxDepth = max(self.maxDepth,currentD)
                return 
            
            left = dC(node.left,currentD+1)
            right = dC(node.right,currentD +1)

        
        
        dC(root,0)

        return self.maxDepth
        

            
            
            