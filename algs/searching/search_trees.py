class TreeNode:

    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_child(self):
        return self.left_child and self.right_child

    def replace_node(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child:
            self.right_child.parent = self

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            pass



class BinraySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, node):
        if key < node.key:
            if node.has_left_child():
                self._put(key, value, self.left_child)
            else:
                node.left_child = TreeNode(key, value, parent=node)
        else:
            if node.has_right_child():
                self._put(key, value, self.right_child)
            else:
                node.right_child = TreeNode(key, value, parent=node)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            rv = self._get(key, self.root)
            if rv:
                return rv.value
        return None

    def _get(self, key, node):
        if not node:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self._get(key, node.left_child)
        else:
            return self._get(key, node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        return False

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("Error, key not found")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not found")

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, node):
        if node.is_leaf():
            if node == node.parent.left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None
        elif node.has_both_child():
            successor = node.find_successor()
            successor.splice_out()
            node.key = successor.key
            node.value = successor.value
        else:
            if node.has_left_child():
                if node.is_left_child():
                    node.left_child.parent = node.parent
                    node.parent.left_child = node.left_child
                elif node.is_right_child():
                    node.left_child.parent = node.parent
                    node.parent.right_child = node.left_child
                else:
                    node.replace_node(node.left_child.key,
                                      node.left_child.value,
                                      node.left_child.left_child,
                                      node.left_child.right_child)
            else:
                if node.is_left_child():
                    node.right_child.parent = node.parent
                    node.parent.left_child = node.right_child
                elif node.is_right_child():
                    node.right_child.parent = node.parent
                    node.parent.right_child = node.right_child
                else:
                    node.replace_node(node.right_child.key,
                                      node.right_child.value,
                                      node.right_child.left_child,
                                      node.right_child.right_child)
