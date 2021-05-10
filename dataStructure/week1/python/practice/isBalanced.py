from stacks import Stack


def is_balanced(string):
    open_pairs = ['(', '[', '{']
    closed_pairs = [')', ']', '}']
    stack = Stack()

    for char in string:
        if char in open_pairs:
            stack.push(char)

        else:

            if stack.empty():
                return False

            for i in range(len(closed_pairs)):
                if char == closed_pairs[i]:
                    if stack.top() == open_pairs[i]:
                        stack.pop()
                    else:
                        return False
    return stack.empty()


if __name__ == '__main__':
    print(is_balanced('([])[]()'))
    print(is_balanced('((([([])])))'))
    print(is_balanced('([]]()'))
    print(is_balanced(']['))
    print(is_balanced('((((([}[}[}([[[}}}}[[}]]]]])]]])))))'))
