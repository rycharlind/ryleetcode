class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf  # True if the node is a leaf
        self.keys = []  # List of keys
        self.children = []  # List of child nodes


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t  # Minimum degree (defines the range for the number of keys)

    def search(self, node, k):
        i = 0
        # Find the first key greater than or equal to k
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        # If the found key is equal to k, return the node and index
        if i < len(node.keys) and node.keys[i] == k:
            return node, i
        # If the key is not found here and this is a leaf node
        if node.leaf:
            return None
        # Go to the appropriate child
        return self.search(node.children[i], k)

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:  # If root is full, split it
            new_root = BTreeNode()
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            # Insert the key in the leaf node in sorted order
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            # Find the child to recurse on
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:  # If the child is full, split it
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def split_child(self, node, i):
        t = self.t
        y = node.children[i]
        z = BTreeNode(y.leaf)
        node.children.insert(i + 1, z)
        node.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def traverse(self, node):
        if node is not None:
            for i in range(len(node.keys)):
                if not node.leaf:
                    self.traverse(node.children[i])
                print(node.keys[i], end=" ")
            if not node.leaf:
                self.traverse(node.children[len(node.keys)])


# Example usage
if __name__ == "__main__":
    t = 3  # Minimum degree of the B-Tree
    btree = BTree(t)

    # Insert elements into the B-Tree
    for value in [10, 20, 5, 6, 12, 30, 7, 17]:
        btree.insert(value)

    # Traverse the B-Tree
    print("Traversal of the B-Tree:")
    btree.traverse(btree.root)

    # Search for a key in the B-Tree
    key_to_search = 6
    result = btree.search(btree.root, key_to_search)
    if result:
        print(f"\nKey {key_to_search} found in the B-Tree")
    else:
        print(f"\nKey {key_to_search} not found in the B-Tree")