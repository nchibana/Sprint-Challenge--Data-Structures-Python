from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length != self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current is None:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                if self.current.next is not None:
                    self.current.next.value = item
                    self.current = self.current.next
                else:
                    self.storage.head.value = item
                    self.current = self.storage.head
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        curr_node = self.storage.head
        for _ in range(self.storage.length):
            list_buffer_contents.append(curr_node.value)
            curr_node = curr_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = [0]*capacity

    def append(self, item):
        if self.current is None:
            self.storage.pop(0)
            self.storage.insert(0, item)
            self.current = 0
        else:
            if self.current <= self.capacity-2:
                self.storage[self.current + 1] = item
                self.current += 1
            else:
                self.storage[0] = item
                self.current = 0

    def get(self):
        return self.storage
