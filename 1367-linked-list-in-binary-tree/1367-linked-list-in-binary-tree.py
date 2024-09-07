# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def is_subpath(node, vertex):
            if not node:
                return True
            if not vertex or vertex.val != node.val:
                return False
            node = node.next
            return is_subpath(node, vertex.left) or is_subpath(node, vertex.right)

        def preorder(vertex):
            if not vertex:
                return False
            if vertex.val == head.val and is_subpath(head, vertex):
                return True
            return preorder(vertex.left) or preorder(vertex.right)

        return preorder(root)
