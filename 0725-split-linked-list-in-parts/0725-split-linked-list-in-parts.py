# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        node_count = 0
        node = head
        while node:
            node_count += 1
            node = node.next
        parts = []
        quotient, remainder = divmod(node_count, k)
        for i in range(k):
            part_length = quotient + (1 if i < remainder else 0)
            part = head
            tail = None
            for _ in range(part_length):
                tail = head
                head = head.next
            if tail:
                tail.next = None
            parts.append(part)
        return parts
