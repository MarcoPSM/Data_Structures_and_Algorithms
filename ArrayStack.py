class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()


def is_matched(expr):
    """ Function for matching delimiters in an arithmetic expression.
    Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['
    righty = ')}]'
    stack = ArrayStack()
    for c in expr:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.is_empty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return stack.is_empty()


def is_matched_html(raw):
    stack = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.tag.startswith('/'):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False
        j = raw.find('<', k+1)
        return stack.is_empty()
