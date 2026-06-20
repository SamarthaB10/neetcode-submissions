from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 
        queue = deque([root]) #control the order 
        res = []


        while len(queue) > 0: 
            n = len(queue)
            lev = [] 

            for _ in range(n): 
                node = queue.popleft() 

                lev.append(node.val)
                
                for child in [node.left,node.right]:
                    if child is not None :
                        queue.append(child)
                    
            res.append(lev)
        return res


            