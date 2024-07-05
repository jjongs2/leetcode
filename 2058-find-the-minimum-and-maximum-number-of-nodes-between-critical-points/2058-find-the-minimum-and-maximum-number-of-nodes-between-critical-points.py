from math import inf


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        min_distance = inf
        first_index, last_index = 0, 0
        index = 1
        left = head
        node = head.next
        while node and (right := node.next):
            if left.val < node.val > right.val or left.val > node.val < right.val:
                if last_index > 0:
                    min_distance = min(min_distance, index - last_index)
                else:
                    first_index = index
                last_index = index
            index += 1
            left = node
            node = right
        if first_index == last_index:
            return [-1, -1]
        return [min_distance, last_index - first_index]
