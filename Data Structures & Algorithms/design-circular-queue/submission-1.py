class Node:
    def __init__(self, key = 0):
        self.key = key
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.first = None
        self.last = None
        self.size = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count < self.size:
            self.count += 1 
            if not self.first:
                self.first = Node(value)
                self.last = Node(value)
            elif not self.first.next:
                new_node = Node(value)
                self.first.next = new_node
                self.last = new_node
                self.last.next = self.first
            else:
                new_node = Node(value)
                self.last.next = new_node
                self.last = new_node
                self.last.next = self.first
            return True
        else:
            return False
            

    def deQueue(self) -> bool:
        if self.first:
            self.count -= 1 
            tmp = self.first.next
            self.first.next = None
            self.first = tmp
            self.last.next = self.first
            return True
        else:
            return False
        

    def Front(self) -> int:
        if self.first:
            return self.first.key
        else:
            return -1

    def Rear(self) -> int:
        if self.first:
            return self.last.key
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        print(self.count)
        if self.count == self.size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()