import string
import operator


def is_circular_rotation(s, t):
    """1.2.6
    check is s and t is circular rotation
    >>> s, t = 'ACTGACG', 'TGACGAC'
    >>> is_circular_rotation(s, t)
    True
    >>> is_circular_rotation(s, 'TT')
    False
    """
    return len(s) == len(t) and ((s + s).find(t) != -1)


def parentheses(text):
    """1.3.4
    check parentheses
    >>> s = '[()]{}{[()()]}'
    >>> parentheses(s)
    True
    >>> s = '[(])'
    >>> parentheses(s)
    False
    """
    if len(text) % 2 != 0:
        return False

    ops = []
    for c in text:
        if c in ('(', '[', '{'):
            ops.append(c)
        else:
            op = ops.pop()
            if c == ')':
                if op != '(':
                    return False
            elif c == ']':
                if op != '[':
                    return False
            else:
                if op != '{':
                    return False
    return True


def complete(expression):
    """
    complete expression
    >>> s = '1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )'
    >>> complete(s)
    '( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) ) )'
    """
    data = []
    operators = []

    for n in expression:
        if n >= '0' and n <= '9':
            data.append(n)
        elif n in ('+', '-', '*', '/'):
            operators.append(n)
        elif n == ')':
            x = data.pop()
            y = data.pop()
            op = operators.pop()
            rv = '( {} {} {} )'.format(y, op, x)
            data.append(rv)

    while operators:
        op = operators.pop()
        x = data.pop()
        y = data.pop()
        rv = '( {} {} {} )'.format(y, op, x)
        data.append(rv)

    return data.pop()


ARITHMETIC_OPERATORS = {
    '*':  operator.mul, '/': operator.truediv,
    '+': operator.add, '-': operator.sub,
    '^': operator.pow, '%': operator.mod,
    '//': operator.floordiv
}


def infix_to_postfix(expression):
    """1.3.10
    """
    prec = {
        '^': 3, '*': 3, '/': 3,
        '+': 2, '-': 2, '(': 1
    }
    postfixchar = string.digits + string.ascii_letters

    operators = []
    postfix = []

    for token in expression.split():
        if token in postfixchar:
            postfix.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top_token = operators.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = operators.pop()
        else:
            while operators and prec[operators[-1]] >= prec[token]:
                postfix.append(operators.pop())
            operators.append(token)

    while operators:
        postfix.append(operators.pop())

    return ' '.join(postfix)


def evaluate_postfix(expression):
    """1.3.11
    """
    token_list = expression.split()

    data = []
    for token in token_list:
        if token in string.digits:
            data.append(int(token))
        else:
            x = data.pop()
            y = data.pop()
            op = ARITHMETIC_OPERATORS[token]
            data.append(op(y, x))

    return data.pop()


def nearest_distance_pair(array):
    """1.4.16
    >>> l = [58.44, 79.18, 0.22, 99.15, 65.97, 26.31, 37.73, 2.82, 71.65, 90.03]
    >>> nearest_distance_pair(l)
    (0.22, 2.82)
    """
    array = sorted(array)
    x, y, distance = None, None, float("inf")

    for n in range(len(array) - 1):
        if (array[n+1] - array[n]) < distance:
            x, y = array[n], array[n+1]
            distance = y - x

    return x, y


def find_peak_element(items):
    size = len(items)

    if size == 1:
        return 0
    if items[0] > items[1]:
        return 0
    if items[size-1] < items[size-2]:
        return size - 1

    low, high = 0, size - 1
    while low < high:
        mid = (high+low) // 2
        if items[mid] < items[mid-1] and items[mid] < items[mid+1]:
            return mid
        elif items[mid] < items[mid+1]:
            low = mid
        else:
            high = mid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
