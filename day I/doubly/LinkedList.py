from abc import ABC as abstract, abstractmethod


class Node:
    def __init__(self, data):
        self.data = data
        self.previous: Node = None  # Additional
        self.next: Node = None


class LinkedList(abstract):
    def __init__(self):
        self.head: Node = None

    def __iter__(self):
        """Initialize the starting point of the iteration

        Returns:
            self: instance of the class
        """
        self.pointer = self.head
        return self

    def __next__(self):
        """Retrieve the current node data and increment the pointer

        Raises:
            StopIteration: stop when the current node doesn't exist

        Returns:
            data: content of the current node
        """
        data = None

        if not self.pointer:
            raise StopIteration

        data = self.pointer.data
        self.pointer = self.pointer.next
        return data

    def __len__(self):
        """Calculate the size of the linked list

        Returns:
            size: total number of node in the linked list
        """
        size = 0
        pointer = self.head

        while pointer:
            size += 1
            pointer = pointer.next

        return size

    def __reverse__(self):
        pointer = self.head

        while pointer.next:
            pointer = pointer.next

        while pointer:
            yield pointer.data
            pointer = pointer.previous

    def index(self, data):
        """Retrieve index of the node which contains the data

        Args:
            data (any): data to search within the linked list

        Returns:
            index: index of the node which contains the data
        """
        index = -1

        if self.count(data) > 0:
            pointer = self.head

            while pointer:
                index += 1

                if pointer.data == data:
                    break

                pointer = pointer.next

        return index

    def count(self, data):
        """Count the total number of time the data appeared in the linked list

        Args:
            data (any): data to count within the linked list

        Returns:
            count: total number of time the data appeared in the linked list
        """
        count = 0
        pointer = self.head

        while pointer:
            if pointer.data == data:
                count += 1

            pointer = pointer.next

        return count

    @abstractmethod
    def append(self, data):
        pass

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def insert(self, position: int, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def remove(self, position: int):
        pass
