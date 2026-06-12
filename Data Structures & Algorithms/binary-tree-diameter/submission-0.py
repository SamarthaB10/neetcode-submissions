# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.m = 0

        def calculateDepth(node): 
            if not node:
                return 0 
            


            leftD = calculateDepth(node.left)
            rightD = calculateDepth(node.right)

            diameter = rightD + leftD

            self.m = max(diameter,self.m)

            return max(leftD, rightD) +1
        
        calculateDepth(root)
        return self.m




'''


'''
