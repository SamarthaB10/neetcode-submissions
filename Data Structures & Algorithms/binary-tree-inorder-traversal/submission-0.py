# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] 
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
            
       

       
'''
go max left: if not root.left -> return , append root 
go back to the parent append(2) 
go down right 
come back up to parent 
traverse down the left 
append 



'''