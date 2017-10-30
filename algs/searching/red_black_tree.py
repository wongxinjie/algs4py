RED = True
BLACK = False


class Node:

    def __init__(self, key, value, size, color):
        self.key = key
        self.value = value
        self.size = size
        self.color = color
        self.left = None
        self.right = None


class RedBlackTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        if node is None:
            return 0
        return node.size

    def is_red(self, node):
        if node is None:
            return BLACK

        return node.color == RED

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        x.size = node.size
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        x.size = node.size
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return x

    def filp_color(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if node is None:
            return None

        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = BLACK

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value, 1, RED)

        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)

        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)

        if self.is_red(node.left) and self.is_red(node.right):
            self.filp_color(node)

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def move_red_left(self, node):
        self.filp_color(node)
        if self.is_red(node.right.left):
            node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
        return node

    def delete_min(self):
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RED

        self.root = self._delete_min(self.root)
        if not self.is_empty():
            self.root.color = BLACK

    def _delete_min(self, node):
        if node.left is None:
            return None

        if not self.is_red(node.left) and not self.is_red(node.left.left):
            node = self.move_red_left(node)

        node.left = self.delete_min(node.left)
        return self.balance(node)

    def balance(self, node):
        if self.is_red(node.right):
            node = self.rotate_left(node)

        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)

        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)

        if self.is_red(node.left) and self.is_red(node.right):
            self.filp_color(node)

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def move_red_right(self, node):
        self.filp_color(node)
        if not self.is_red(node.left.left):
            node = self.rotate_right(node)
        return node

    def delete_max(self):
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RED
        self.root = self._delete_max(self.root)

        if not self.is_empty():
            self.root.color = BLACK

    def _delete_max(self, node):
        if self.is_red(node.left):
            node = self.rotate_right(node)

        if node.right is None:
            return None
        if not self.is_red(node.right) and not node.right.left:
            node = self.move_red_right(node.right)

        node.right = self._delete_max(node.right)
        return self.balance(node)

    def delete(self, key):
        if not self.is_red(self.root.left) and not self.is_red(self.root.right):
            self.root.color = RED

        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color = BLACK

    def _delete(self, node, key):
        if key < node.key:
            if not self.is_red(node.left) and not self.is_red(node.left.left):
                node = self.move_red_left(node)
            node.left = self._delete(node.left, key)
        else:
            if self.is_red(node.left):
                node = self.rotate_right(node)

            if key == node.key and node.right is None:
                return None

            if not self.is_red(node.right) and not self.is_red(node.right.left):
                node = self.move_red_right(node)

            if key == node.key:
                node.value = self._get(node.right, self._min(node.right).key)
                node.key = self._min(node.right).key
                node.right = self._delete_min(node.right)
            else:
                node.right = self._delete(node.right, key)

        return self.balance(node)


if __name__ == "__main__":
    tree = RedBlackTree()
    tree.put('E', 2)
    tree.put('A', 12)
    tree.put('B', 13)
    tree.put('D', 8)
    tree.put('C', 11)

    tree.delete('D')
    print(tree.get('D'))
