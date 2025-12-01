# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.r(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
            
    def r(self, root, sub):
        if (not root) and (not sub):
            return True
        if (not root) or (not sub):
            return False
        return root.val == sub.val and self.r(root.right, sub.right) and self.r(root.left, sub.left)
            
'''
subroot중심으로 탐색
leaf노드들의 자식들은 부모보다작음
state
root에서부터 비교하고
이후에는 크기 비교하면서 subRoot보다 작은 노드는 탐색할 필요없음

'''