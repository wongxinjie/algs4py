import operator


class BinaryTree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert_left(self, key):
        if self.left is None:
            self.left = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.left = self.left
            self.left = t

    def insert_right(self, key):
        if self.right is None:
            self.right = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.right = self.right
            self.right = t

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def get_root_value(self):
        return self.key

    def set_root_value(self, key):
        self.key = key

    def __str__(self):
        return "{} -> L={}, R={}".format(self.key, self.left, self.right)


def preorder(tree):
    if tree:
        print(tree.get_root_value(), end=" ")
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_value(), end=" ")
        inorder(tree.get_right_child())


def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_value(), end=" ")


def build_parse_tree(expression):
    tokens = expression.split()
    stack = []
    tree = BinaryTree('')
    stack.append(tree)
    current_tree = tree

    for token in tokens:
        if token == '(':
            current_tree.insert_left('')
            stack.append(current_tree)
            current_tree = current_tree.get_left_child()
        elif token not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_value(float(token))
            parent = stack.pop()
            current_tree = parent
        elif token in ['+', '-', '*', '/']:
            current_tree.set_root_value(token)
            current_tree.insert_right('')
            stack.append(current_tree)
            current_tree = current_tree.get_right_child()
        elif token == ')':
            current_tree = stack.pop()
        else:
            raise ValueError("invalid token {}".format(token))

    return tree

operators = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}


def evaluate(tree):
    left = tree.get_left_child()
    right = tree.get_right_child()

    if left and right:
        func = operators[tree.get_root_value()]
        return func(evaluate(left), evaluate(right))
    else:
        return tree.get_root_value()


def postorder_eval(tree):
    left, right = None, None
    if tree:
        left = postorder_eval(tree.get_left_child())
        right = postorder_eval(tree.get_right_child())
        if left and right:
            return operators[tree.get_root_value()](left, right)
        else:
            return tree.get_root_value()


def print_expression(tree):
    exp = ""
    if tree:
        if tree.get_left_child():
            exp = '(' + print_expression(tree.get_left_child())
        exp += str(tree.get_root_value())
        if tree.get_right_child():
            exp += print_expression(tree.get_right_child()) + ')'

    return exp


parse_tree = build_parse_tree('( 10 + 4 ) * 3 + ( 7 - 4 ) / 3')
preorder(parse_tree)
print('preorder')
postorder(parse_tree)
print('postorder')
inorder(parse_tree)
print('inorder')
# result = evaluate(parse_tree)
# result = postorder_eval(parse_tree)
# print(result)
# result = print_expression(parse_tree)
# print(result)
