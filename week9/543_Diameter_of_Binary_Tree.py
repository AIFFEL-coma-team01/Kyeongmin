# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
        
        
#         new_root = TreeNode(temp)
#         right = 0
#         left = 0
#         temp1 = new_root
#         temp2 = new_root
        
#         while temp1:
#             # right에는 조건이 필요함.
#             if
#             right += 1
#             temp1 = temp1.right
