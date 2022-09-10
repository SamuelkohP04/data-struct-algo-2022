from enum import Enum
from random import randint


class Color(Enum):
    BLACK = 0
    RED = 1


class Node():
    def __init__(self, item):
        self.item = item
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
        self.color = Color.RED


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = Color.BLACK
        self.root = self.TNULL

    def preorder(self):
        """Pre-order traverse starting from root node
        """
        self.__preorder__(self.root)

    def __preorder__(self, node: Node):
        """Pre-order traverse

        Args:
            node (Node): node to start traverse
        """
        if self.TNULL != node:
            print(node.item, end=' ')
            self.__preorder__(node.left)
            self.__preorder__(node.right)

    def inorder(self):
        """In-order traverse starting from root node
        """
        self.__inorder__(self.root)

    def __inorder__(self, node: Node):
        """In-order traverse

        Args:
            node (Node): node to start traverse
        """
        if self.TNULL != node:
            self.__inorder__(node.left)
            print(node.item, end=' ')
            self.__inorder__(node.right)

    def postorder(self):
        """Post-order traverse starting from root node
        """
        self.__postorder__(self.root)

    def __postorder__(self, node: Node):
        """Post-order traver

        Args:
            node (Node): node to start traverse
        """
        if self.TNULL != node:
            self.__postorder__(node.left)
            self.__postorder__(node.right)
            print(node.item, end=' ')

    def search(self, item):
        """Search an item (data) in the red black tree starting fron the root node

        Args:
            item (Any): item (data) to serach in the red black tree

        Returns:
            Node: the node that contains the item (data)
        """
        return self.__search__(self.root, item)

    def __search__(self, node: Node, item):
        """Search an item (data) in the red black tree

        Args:
            node (Node): node to start searching
            item (Any): item (data) to search in the red black tree

        Returns:
            Node: the node that contains the item (data)
        """
        if self.TNULL == node or node.item == item:
            return node

        if node.item > item:
            return self.__search__(node.left, item)

        return self.__search__(node.right, item)

    def output(self):
        """Output the red black tree starting from the root node
        """
        self.__output__(self.root, '', True)

    def __output__(self, node: Node, indent: str, is_last: bool):
        """Output the red black tree

        Args:
            node (Node): node to start traversing
            indent (str): indent to determine the level of the tree
            is_last (bool): flag to indicate if the node if right node of the parent
        """
        if self.TNULL != node:
            print(indent, end='')

            if is_last:
                print('R----', end='')
                indent += ' \t'
            else:
                print('L----', end='')
                indent += '|\t'

            print(f'{node.item} ({node.color})')
            self.__output__(node.left, indent, False)
            self.__output__(node.right, indent, True)

    def minimum(self, node: Node):
        """Find the minimum value starting from the given node

        Args:
            node (Node): node to start searching for the minimum value

        Returns:
            Node: the node that have the minimum value
        """
        while self.TNULL != node.left:
            node = node.left

        return node

    def maximum(self, node: Node):
        """Find the maximum value starting from the given node

        Args:
            node (Node): node to start searching for the maximum value

        Returns:
            Node: the node that have the maximum value
        """
        while self.TNULL != node.right:
            node = node.right

        return node

    def insert(self, item):
        node = Node(item)
        node.parent: Node = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = Color.RED

        parent: Node = None
        child = self.root

        while self.TNULL != child:
            parent = child

            if node.item < child.item:
                child = child.left
            else:
                child = child.right

        node.parent = parent

        if None == parent:
            self.root = node
        elif node.item < parent.item:
            parent.left = node
        else:
            parent.right = node

        if None == node.parent:
            node.color = Color.BLACK
            return

        if None == node.parent.parent:
            return

        self.rebalance_insert(node)

    def rebalance_insert(self, node: Node):
        while Color.RED == node.parent.color:
            if node.parent == node.parent.parent.right:
                left = node.parent.parent.left

                if Color.RED == left.color:
                    left.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.rotate_left(node.parent.parent)
            else:
                right = node.parent.parent.right

                if right.color == Color.RED:
                    right.color = Color.BLACK
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self.rotate_right(node.parent.parent)

            if node == self.root:
                break

        self.root.color = Color.BLACK

    def delete(self, item):
        self.__delete__(self.root, item)

    def __delete__(self, node: Node, item):
        a = self.TNULL

        while self.TNULL != node:
            if node.item == item:
                a = node

            if node.item <= item:
                node = node.right
            else:
                node = node.left

        if self.TNULL == a:
            print(f'{item} doesn\'t exist in the tree')
            return

        b = a
        b_original_color = b.color

        if self.TNULL == a.left:
            c = a.right
            self.transplant(a, a.right)

        elif self.TNULL == a.right:
            c = a.left
            self.transplant(a, a.left)

        else:
            b = self.minimum(a.right)
            b_original_color = b.color
            c = b.right

            if b.parent == a:
                c.parent = b
            else:
                self.transplant(b, b.right)
                b.right = a.right
                b.right.parent = b

            self.transplant(a, b)
            b.left = a.left
            b.left.parent = b
            b.color = a.color

        if Color.BLACK == b_original_color:
            self.rebalance_delete(c)

    def rebalance_delete(self, node: Node):
        while self.root != node and Color.BLACK == node.color:
            if node == node.parent.left:
                right = node.parent.right

                if Color.RED == right.color:
                    right.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rotate_left(node.parent)

                if Color.BLACK == right.left.color and Color.BLACK == right.right.color:
                    right.color = Color.RED
                    node = node.parent
                else:
                    if Color.BLACK == right.right.color:
                        right.left.color = Color.BLACK
                        right.color = Color.RED
                        self.rotate_right(right)

                    right.color = node.parent.color
                    node.parent.color = Color.BLACK
                    right.right.color = Color.BLACK
                    self.rotate_left(node.parent)
                    node = self.root
            else:
                left = node.parent.left

                if Color.RED == left.color:
                    left.color = Color.BLACK
                    node.parent.color = Color.RED
                    self.rotate_right(node.parent)

                if Color.BLACK == left.right.color:
                    left.color = Color.RED
                    node = node.parent
                else:
                    if Color.BLACK == left.left.color:
                        left.right.color = Color.BLACK
                        left.color = Color.RED
                        self.rotate_left(left)

                    left.color = node.parent.color
                    node.parent.color = Color.BLACK
                    left.left.color = 0
                    self.rotate_right(node.parent)
                    node = self.root

        node.color = Color.BLACK

    def transplant(self, a: Node, b: Node):
        if None == a.parent:
            self.root = b
        elif a == a.parent.left:
            a.parent.left = b
        else:
            a.parent.right = b
        b.parent = a.parent

    def rotate_left(self, node: Node):
        right = node.right
        node.right = right.left

        if self.TNULL != right.left:
            right.left.parent = node

        right.parent = node.parent

        if None == node.parent:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right

        right.left = node
        node.parent = right

    def rotate_right(self, node: Node):
        left = node.left
        node.left = left.right

        if self.TNULL != left.right:
            left.right.parent = node

        left.parent = node.parent

        if None == node.parent:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left

        left.right = node
        node.parent = left


if __name__ == '__main__':
    tree = RedBlackTree()

    test_data = [randint(0, 100) for _ in range(randint(10, 30))]
    print(test_data)

    [tree.insert(i) for i in test_data]
    tree.output()

    delete_data = test_data[randint(0, len(test_data) - 1)]
    print(delete_data)
    tree.delete(delete_data)
    tree.output()
