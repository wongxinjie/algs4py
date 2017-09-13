class ListStack:

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def __iter__(self):
        for item in reversed(self.__items):
            yield item


class Node:
    __slots__ = ('value', 'next')

    def __init__(self, value):
        self.value = value
        self.next = None


class Collection:

    def size(self):
        return self._size

    def is_empty(self):
        return self._head is None

    def __iter__(self):
        _iter = self._head
        while _iter is not None:
            value = _iter.value
            _iter = _iter.next
            yield value


class Stack(Collection):

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value


class Queue(Collection):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value):
        tail = self._tail
        self._tail = Node(value)

        if self.is_empty():
            self._head = self._tail
        else:
            tail.next = self._tail

        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        self._size -= 1
        return value


class Bag(Collection):

    def __init__(self):
        self._head = None
        self._size = 0

    def add(self, value):
        tail = self._head
        self._head = Node(value)
        self._head.next = tail
        self._size += 1

s = Stack()
s.pop()

