from random import randint


class Node:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.key_list = []
        self.data_list: list[Node] = []

    @property
    def key_size(self):
        return len(self.key_list)


class BTree:
    def __init__(self, t):
        self.root = Node(True)
        self.t = t
        self.min_key_size = t - 1
        self.max_key_size = 2 * t - 1

    def insert(self, data):
        """
        Insert the data into the binary tree.
        If the root key size reached the maximum capacity, 
            move the root to the newly created node data list,
            perform the spliting operation,
            finally insert the data into the tree
        Else directly insert the data into the tree

        Args:
            data (Any): data to insert to the binary tree
        """
        root = self.root

        if root.key_size == self.max_key_size:
            node = Node()
            node.data_list.insert(0, root)

            self.root = node
            self.split_data_list(node, 0)
            self.insert_non_full(node, data)

        else:
            self.insert_non_full(root, data)

    def insert_non_full(self, parent: Node, data):
        """
        Insert the data into the binary tree
        If the parent node is a leaf execute leaf insertion method
        Else execute the non leaf insertion method

        Args:
            parent (Node): target node to insert the data
            data (Any): data to insert to the binary tree
        """
        executable = self.insert_leaf if parent.is_leaf else self.insert_non_leaf
        executable(parent, data)

    def insert_leaf(self, parent: Node, data):
        """Insert the data into the node key list

        Args:
            parent (Node): target node to insert the data
            data (Any): data to insert to the binary tree
        """
        i = parent.key_size - 1
        parent.key_list.append(None)

        while i >= 0 and data < parent.key_list[i]:
            parent.key_list[i + 1] = parent.key_list[i]
            i -= 1
        parent.key_list[i + 1] = data

    def insert_non_leaf(self, parent: Node, data):
        """Insert the data into the node data list

        Args:
            parent (Node): target node to insert the data
            data (Any): data to insert to the binary tree
        """
        i = parent.key_size - 1

        while i >= 0 and data < parent.key_list[i]:
            i -= 1
        i += 1

        # Check if the node key size reached maximum capacity
        if parent.data_list[i].key_size == self.max_key_size:
            self.split_data_list(parent, i)  # Perform the spliting operation

            # Check if the data is larger than selected key after performed the spliting operation
            if data > parent.key_list[i]:
                i += 1  # Increase by 1 if the data is larger

        # Insert the data into the node data list
        self.insert_non_full(parent.data_list[i], data)

    def split_data_list(self, parent: Node, index):
        """Split the binary tree node

        Args:
            parent (Node): target node to split
            index (_type_): index of the children node to split
        """
        take = parent.data_list[index]
        node = Node(take.is_leaf)

        # Insert the created node into the data list
        # Move the children middle key to the parent key list
        parent.data_list.insert(index + 1, node)
        parent.key_list.insert(index, take.key_list[self.min_key_size])

        # Move the second half portion of the 'take' key list to the created node
        # Keep only the first half portion of the 'take' key list
        node.key_list = take.key_list[self.t: self.max_key_size]
        take.key_list = take.key_list[0: self.min_key_size]

        # If the node is a non leaf node
        # Move the second half portion of the 'take' data list to the created node
        # Keep only the first half portion of the 'take' data list
        if not take.is_leaf:
            node.data_list = take.data_list[self.t: self.max_key_size + 1]
            take.data_list = take.data_list[0: self.min_key_size + 1]

    def print_tree(self, parent: Node, level=0):
        print("Level ", level, " ", len(parent.key_list), end=":")
        for i in parent.key_list:
            print(i, end=" ")
        print()
        level += 1
        if len(parent.data_list) > 0:
            for i in parent.data_list:
                self.print_tree(i, level)


if __name__ == '__main__':
    tree = BTree(3)
    test_data = [randint(0, 100) for _ in range(randint(10, 30))]

    [tree.insert(i) for i in test_data]

    tree.print_tree(tree.root)
