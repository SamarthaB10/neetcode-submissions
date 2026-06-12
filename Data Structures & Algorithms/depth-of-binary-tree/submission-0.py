# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.m = 0
        
        def dfs(node,curD):
            if not node:
                self.m = max(self.m,curD) 
                return
            
            dfs(node.left,curD +1)
            dfs(node.right,curD +1)
        
        dfs(root,0)
        return self.m
           


            
            
            
            
