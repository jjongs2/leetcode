# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from heapq import heappush, heappushpop


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        q = deque([root])
        while q:
            level_sum = sum(map(lambda x: x.val, q))
            if len(heap) < k:
                heappush(heap, level_sum)
            else:
                heappushpop(heap, level_sum)
            for _ in range(len(q)):
                node = q.popleft()
                q.extend(child for child in (node.left, node.right) if child)
        return heap[0] if len(heap) == k else -1
