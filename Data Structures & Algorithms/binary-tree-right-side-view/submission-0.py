# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = [] 

        while len(q) > 0: 
            level =[] 

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res.append(level[-1])
        
        return res
            
                
                
            

'''

root = [1,2,3,null,4,null,5]

BFS 

if left and right -> pick right 
if only left -> pick left 



'''