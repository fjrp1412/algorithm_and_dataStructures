class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextNode = None


class Stack:

    def __init__(self, value=None):
        self._head = Node(value)

    def push(self, value):
        if(self._head.value is None):
            self._head.value = value

        node = Node(value)
        node.nextNode = self._head
        self._head = node

    def top(self):
        return self._head.value

    def pop(self):
        if(self._head.value is None):
            return None

        head = self._head
        self._head = head.nextNode
        return head.value

    def empty(self):
        return self._head.value is None

    def __str__(self):
        actual = self._head
        result = ""
        if(actual.value is None):
            return "the stack is empty"

        while(actual.nextNode is not None):
            result += f'{actual.value} '
            actual = actual.nextNode

        return result


if __name__ == '__main__':
    pass
