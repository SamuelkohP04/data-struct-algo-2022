from LinkedList import LinkedList, Node


class CircularDoubly(LinkedList):
    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            self.head.previous = node
            self.head.next = node
            return

        pointer = self.head

        while pointer:
            pointer = pointer.next

            if pointer.next == self.head:
                break

        pointer.next = node
        node.previous = pointer
        node.next = self.head
        self.head.previous = node

    def push(self, data):
        node = Node(data)
        node.next = self.head
        node.previous = self.head.previous
        self.head.previous.next = node
        self.head.previous = node
        self.head = node

    def insert(self, position: int, data):
        index = 0
        pointer = self.head

        while position > index and pointer:
            index += 1
            pointer = pointer.next

            if pointer.next == self.head:
                break

        node = Node(data)
        node.next = pointer.next
        node.previous = pointer
        pointer.next.previous = node
        pointer.next = node

    def pop(self):
        pointer = self.head

        while pointer:
            pointer = pointer.next

            if pointer.next == self.head:
                break

        pointer.previous.next = pointer.next
        pointer.next.previous = pointer.previous
        pointer.next = None
        pointer.previous = None

        return pointer.data

    def remove(self, position: int):
        index = 0
        pointer = self.head

        while position > index and pointer:
            index += 1
            pointer = pointer.next

            if pointer.next == self.head:
                break

        pointer.previous.next = pointer.next
        pointer.next.previous = pointer.previous
        pointer.next = None
        pointer.previous = None

        return pointer.data


if __name__ == '__main__':
    singly = CircularDoubly()
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
