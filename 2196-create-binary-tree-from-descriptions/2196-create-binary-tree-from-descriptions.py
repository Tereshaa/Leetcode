# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes={}
        children=set()
        for par,chd,is_left in descriptions:
            children.add(chd)
            if par not in nodes:
                nodes[par]=TreeNode(par)
            if chd not in nodes:
                nodes[chd]=TreeNode(chd)
            if is_left:
                nodes[par].left=nodes[chd]
            else:
                nodes[par].right=nodes[chd]
         
        for p,c,l in descriptions:
            if p not in children:
                return nodes[p]
        