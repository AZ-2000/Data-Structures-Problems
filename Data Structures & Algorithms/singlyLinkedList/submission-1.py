class Node:
    def __init__(self, val = 0, next_node = None):
        self.val = val
        self.next_node = next_node

class LinkedList:

    def __init__(self):
        self.root = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.root
        for i in range(index):
            curr = curr.next_node
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.root)
        self.root = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.root:
            self.root = new_node
        else:
            curr = self.root
            while curr.next_node:
                curr = curr.next_node
            curr.next_node = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.root = self.root.next_node
            self.size -= 1
            return True
        else:
            curr = self.root
            for i in range(index-1):
                curr = curr.next_node
            rem = curr.next_node
            curr.next_node = rem.next_node
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.root
        while curr is not None:
            res.append(curr.val)
            curr = curr.next_node

        return res
        
