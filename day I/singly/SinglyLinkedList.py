from LinkedList import LinkedList, Node


class Singly(LinkedList):
    def append(self, data):
        """Create a new node containing the data then append to the linked list

        Args:
            data (any): data to be append to the linked list
        """
        node = Node(data)

        if not self.head:
            self.head = node
            return

        pointer = self.head

        while pointer.next:
            pointer = pointer.next

        pointer.next = node

    def push(self, data):
        """Create a new node containing the data then add it to the front of the linked list

        Args:
            data (any): data to be push to the linked list
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, position: int, data):
        """Create a new node containing the data then insert (after the position) it to the linked list 

        Args:
            position (int): position of the data to be inserted
            data (any): data to be added to the linked list
        """
        index = 0
        pointer = self.head

        while position > index and pointer.next:
            pointer = pointer.next
            index += 1

        node = Node(data)
        node.next = pointer.next
        pointer.next = node

    def pop(self):
        """Remove the last node from the linked list then return the data

        Returns:
            data: data of the removed node
        """
        left: Node = None
        right: Node = self.head

        while right.next:
            left = right
            right = right.next

        left.next = None
        return right.data

    def remove(self, position: int):
        """Remove the node from the linked list then return the data

        Returns:
            data: data of the removed node
        """
        index = 0
        left: Node = None
        right: Node = self.head

        while position > index and right.next:
            left = right
            right = right.next
            index += 1

        left.next = right.next
        return right.data


if __name__ == '__main__':
    singly = Singly()
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
