class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev) # 두 노드간의 차 중 최소값
        self.prev = root.val #

        if root.right:
            self.minDiffInBST(root.right)

        return self.result
