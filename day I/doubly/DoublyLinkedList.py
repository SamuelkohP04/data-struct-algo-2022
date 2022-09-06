from LinkedList import LinkedList, Node


class Doubly(LinkedList):
    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return

        pointer = self.head

        while pointer.next:
            pointer = pointer.next

        pointer.next = node
        node.previous = pointer

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head.previous = node
        self.head = node

    def insert(self, position: int, data):
        index = 0
        pointer = self.head

        while position > index and pointer.next:
            pointer = pointer.next
            index += 1

        node = Node(data)
        node.next = pointer.next
        node.previous = pointer
        pointer.next.previous = node
        pointer.next = node

    def pop(self):
        pointer = self.head

        while pointer.next:
            pointer = pointer.next

        pointer.previous.next = None
        pointer.previous = None
        return pointer.data

    def remove(self, position: int):
        index = 0
        pointer = self.head

        while position > index and pointer.next:
            pointer = pointer.next
            index += 1

        pointer.previous.next = pointer.next
        pointer.next.previous = pointer.previous
        pointer.previous = None
        pointer.next = None
        return pointer.data


if __name__ == '__main__':
    singly = Doubly()
    singly.append(0)
    singly.push(1)
    singly.append(2)
    singly.append(13)
    singly.append(3)
    singly.push(4)
    singly.insert(1, 10)
    singly.pop()
    singly.append(5)
    singly.append(6)
    singly.push(7)
    singly.insert(6, 11)
    singly.remove(4)
    singly.push(12)
    singly.pop()
    singly.append(8)
    singly.append(9)
    singly.insert(4, 14)
    singly.insert(0, 15)
    singly.insert(11, 16)

    print([item for item in singly])
    print([item for item in singly.__reverse__()])
