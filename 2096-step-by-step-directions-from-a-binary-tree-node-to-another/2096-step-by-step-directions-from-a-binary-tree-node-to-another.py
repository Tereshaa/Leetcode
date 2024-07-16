# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
         def findLCA(node):
            if not node or node.val == startValue or node.val == destValue:
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if left and right:
                return node
            return left if left else right
        
         lca = findLCA(root)
        
        
         def findPath(node, value, path):
            if not node:
                return False
            if node.val == value:
                return True
            path.append('L')
            if findPath(node.left, value, path):
                return True
            path.pop()
            
            path.append('R')
            if findPath(node.right, value, path):
                return True
            path.pop()
            return False
        
         path_to_start = []
         findPath(lca, startValue, path_to_start)
         path_to_dest = []
         findPath(lca, destValue, path_to_dest)
        
      
         up_moves = ['U'] * len(path_to_start)
       
         down_moves = path_to_dest
        
         return ''.join(up_moves + down_moves)
