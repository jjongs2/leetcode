from math import gcd

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev, curr = head, head.next
        while curr:
            prev.next = ListNode(val=gcd(prev.val, curr.val), next=curr)
            prev, curr = curr, curr.next
        return head
