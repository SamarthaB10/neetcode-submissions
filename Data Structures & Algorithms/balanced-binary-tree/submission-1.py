# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True  
        def checkD(node):

            if not node:
                return 0

            left = checkD(node.left)
            right = checkD(node.right)


            if abs(right-left) > 1:
                self.isBalanced = False 

            return max(left,right) +1

        checkD(root)
        return self.isBalanced

            


        
        
