# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        targets = set(nums)
        dummy = ListNode(next=head)
        prev = dummy
        while curr := prev.next:
            if curr.val in targets:
                prev.next = curr.next
            else:
                prev = curr
        return dummy.next
