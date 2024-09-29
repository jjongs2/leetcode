class ListNode:
    def __init__(
        self,
        value: set = set(),
        prev_node: ListNode | None = None,
        next_node: ListNode | None = None,
    ):
        self.value = value
        self.prev = prev_node or self
        self.next = next_node or self

    def insert_to_list(self):
        self.prev.next = self
        self.next.prev = self

    def remove_from_list(self):
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:
    def __init__(self):
        self.counts = dict()
        self.nodes = {0: ListNode({"DUMMY"})}

    def inc(self, key: str) -> None:
        count = self.counts.get(key, 0)
        node = self.nodes[count]
        self._change_count(key, count, count + 1, node, node.next)

    def dec(self, key: str) -> None:
        count = self.counts[key]
        node = self.nodes[count]
        self._change_count(key, count, count - 1, node.prev, node)
        if count == 1:
            del self.counts[key]

    def getMaxKey(self) -> str:
        return next(iter(self.nodes[0].prev.value)) if self.counts else ""

    def getMinKey(self) -> str:
        return next(iter(self.nodes[0].next.value)) if self.counts else ""

    def _change_count(
        self,
        key: str,
        count: int,
        new_count: int,
        prev_node: ListNode,
        next_node: ListNode,
    ) -> None:
        if new_count in self.nodes:
            self.nodes[new_count].value.add(key)
        else:
            new_node = ListNode({key}, prev_node, next_node)
            new_node.insert_to_list()
            self.nodes[new_count] = new_node
        node = self.nodes[count]
        node.value.discard(key)
        if not node.value:
            node.remove_from_list()
            del self.nodes[count]
        self.counts[key] = new_count


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
