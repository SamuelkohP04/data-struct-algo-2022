from abc import ABC as abstract, abstractmethod


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None
        self.previous: Node = None


class LinkedList(abstract):
    def __init__(self):
        self.head: Node = None

    def __iter__(self):
        pointer = self.head

        while pointer:
            yield pointer.data
            pointer = pointer.next

            if pointer == self.head:
                break

    def __len__(self):
        size = 0
        pointer = self.head

        while pointer:
            size += 1
            pointer = pointer.next

            if pointer == self.head:
                break

        return size

    def index(self, data):
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
        count = 0
        pointer = self.head

        while pointer:
            if pointer.data == data:
                count += 1

            pointer = pointer.next

            if pointer == self.head:
                break

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
