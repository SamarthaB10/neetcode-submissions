# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root:
            return True 
        if not subRoot or not root:
            return False 
        
        
        val = subRoot.val
        
        
        def dfs(node):
            if not node:
                return False 
            
            if node.val == val and sameTree(node,subRoot):
               return True
            #currently here 
            y = dfs(node.left)
            z = dfs(node.right)
        
            return y or z
        
        def sameTree(node,subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False  
            if node.val != subRoot.val:
                return False 
             
            return sameTree(node.left,subRoot.left) and sameTree(node.right,subRoot.right)
        
        x = dfs(root)

        return x



        


'''
check if node.val == top node
false? 
check left
'''


        
            



'''
find top node
dfs through list
compare with dfs of subRoot



'''