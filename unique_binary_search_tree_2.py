# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def create_BST(left, right):
            if left == right:
                return [None]
            bsts = []
            for mid in range(left, right):
                for left_child in create_BST(left, mid):
                    for right_child in create_BST(mid+1, right):
                        new_bst = TreeNode(mid)
                        new_bst.left = left_child
                        new_bst.right = right_child
                        bsts.append(new_bst)
            return bsts
        return create_BST(1, n+1)
                        
