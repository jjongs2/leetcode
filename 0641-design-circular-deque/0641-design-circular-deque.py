class ListNode:
    def __init__(
        self,
        value: int = -1,
        prev_node: ListNode | None = None,
        next_node: ListNode | None = None,
    ):
        self.value = value
        self.prev = prev_node if prev_node else self
        self.next = next_node if next_node else self


class MyCircularDeque:
    def __init__(self, k: int):
        self.size = 0
        self.max_size = k
        self.dummy = ListNode()

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        self._insert_node(ListNode(value, self.dummy, self.dummy.next))
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        self._insert_node(ListNode(value, self.dummy.prev, self.dummy))
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        self._delete_node(self.dummy.next)
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        self._delete_node(self.dummy.prev)
        return True

    def getFront(self) -> int:
        return self.dummy.next.value if self.size > 0 else -1

    def getRear(self) -> int:
        return self.dummy.prev.value if self.size > 0 else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

    def _insert_node(self, node: ListNode) -> None:
        node.prev.next = node
        node.next.prev = node
        self.size += 1

    def _delete_node(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
