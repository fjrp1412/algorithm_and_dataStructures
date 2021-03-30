
class Node:
    def __init__(self, value):
        self.value = value
        self.nextNode = None


class LinkedList:

    def __init__(self, value=None):
        node = Node(value)
        self._head = node

    def __iterateList(self):
        actual = self._head
        while(actual.nextNode is not None):
            actual = actual.nextNode
        return actual

    @property
    def head(self):
        if(self._head is None):
            return None

        return self._head.value

    def pushFront(self, value):
        if(self._head.value is None):
            self._head = Node(value)
            return

        node = Node(value)
        node.nextNode = self._head
        self._head = node

    def pushBack(self, value):
        if(self._head.value is None):
            self._head = Node(value)
            return

        node = Node(value)
        actual = self.__iterateList()
        actual.nextNode = node

    def popHead(self):
        if(self._head.value is None):
            return None
        head = self._head
        self._head = head.nextNode
        return head.value

    def getBack(self):
        if(self._head.value is None):
            return None

        return self.__iterateList().value

    def popBack(self):
        if(self._head.value is None):
            return None

        actual = self._head
        while(actual.nextNode.nextNode is not None):
            actual = actual.nextNode
        value = actual.nextNode.value
        actual.nextNode = None
        return value

    def find(self, value):
        actual = self._head
        while(actual is not None):
            if(actual.value == value):
                return True
            actual = actual.nextNode

        return False

    def remove(self, value):
        actual = self._head

        if(actual is None):
            raise ValueError(f'the element {value} is not in list')

        if(actual.value == value):
            self._head = actual.nextNode

        else:
            while(actual.nextNode is not None):
                if(actual.nextNode.value == value):
                    break
                actual = actual.nextNode

            if(actual.nextNode is None):
                raise ValueError(f'the element {value} is not in list')

            try:
                actual.nextNode = actual.nextNode.nextNode
            except AttributeError:
                actual.nextNode = None

    def is_empty(self):
        return self._head.value is None

    def __str__(self):
        actual = self._head
        result = ""
        while(actual is not None):
            result += f'{actual.value} '
            actual = actual.nextNode

        return result


if __name__ == '__main__':
    array = LinkedList()
    print(array.is_empty())
    array.pushFront(1)
    array.pushBack(2)
    array.pushFront(3)
    array.pushBack(4)
    print(array)
    print(array.is_empty())
