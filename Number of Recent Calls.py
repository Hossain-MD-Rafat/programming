# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, TreeNode) -> int:
        l = 0
        count = 0
        while(1):
            if TreeNode[2*l+1]:
                l=2*l+1
                count += 1
            elif TreeNode[2*l+2]:
                l = 2 * l + 2
                count += 1