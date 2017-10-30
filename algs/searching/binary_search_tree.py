class Node:

    def __init__(self, key, value, size):
        self.key = key
        self.value = value
        self.size = size
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return node.size

    # def get(self, key):
    #     return self._get(self.root, key)

    # def _get(self, node, key):
    #     if node is None:
    #         return None

    #     if key < node.key:
    #         return self._get(node.left, key)
    #     elif key > node.key:
    #         return self._get(node.right, key)
    #     else:
    #         return node.value

    def get(self, key):
        node = self.root

        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value

    def put(self, key, value):
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value, 1)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def max(self):
        return self._max(self.root).key

    def _max(self, node):
        if node.right is None:
            return node
        return self._max(node.right)

    def min(self):
        return self._min(self.root).key

    def _min(self, node):
        if node.left is None:
            return node
        return self._min(node.left)

    def floor(self, key):
        x = self._floor(self.root, key)
        return x if x is None else x.key

    def _floor(self, node, key):
        if node is None:
            return node

        if key == node.key:
            return node
        elif key < node.key:
            return self._floor(node.left, key)

        n = self._floor(node.right, key)
        if n is not None:
            return n
        else:
            return node

    def select(self, k):
        return self._select(self.root, k)

    def _select(self, node, k):
        if node is None:
            return node
        r = self._size(node.left)
        if r < k:
            return self._select(node.left, k)
        elif r > k:
            return self._select(node.right, r - k - 1)
        else:
            return node

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        if node is None:
            return 0

        if key < node.key:
            return self._rank(self.left, key)
        elif key > node.key:
            return 1 + self._size(node.left) + self._rank(node.right, key)
        else:
            return self._size(node.left)

    def delete_min(self):
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None:
            return node.right

        node.left = self._delete_min(node.left)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right

            t = node
            node = self._min(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.key)
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key)

    def prefixorder(self, node):
        if node is None:
            return
        print(node.key)
        self.prefixorder(node.left)
        self.prefixorder(node.right)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        right_height = self._height(node.right)
        left_heigh = self._height(node.left)
        _height = right_height if right_height > left_heigh else left_heigh
        return _height + 1


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.put('E', 2)
    tree.put('A', 12)
    tree.put('B', 13)
    tree.put('D', 8)
    tree.put('C', 11)
    print(tree.height())

    tree.delete('D')
    print(tree.get('D'))
    print(tree.height())
