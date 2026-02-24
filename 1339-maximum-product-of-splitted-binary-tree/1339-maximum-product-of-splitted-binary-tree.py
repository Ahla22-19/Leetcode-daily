# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        all_sums = []
        def tree_sum(node):
            if node is None:
                return 0
            
            left_s = tree_sum(node.left)
            right_s = tree_sum(node.right)

            current_s = left_s + right_s + node.val
            all_sums.append(current_s)
            return current_s

        total_sum = tree_sum(root)
        best = 0

        for s in all_sums:
            best = max(best, s* (total_sum - s))

        return best % (10**9 + 7)