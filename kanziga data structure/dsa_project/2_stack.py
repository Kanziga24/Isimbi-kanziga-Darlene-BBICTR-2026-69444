"""
Task 2: Stack
Contributor: Member B

Stack implemented from scratch (list used only as raw storage, not as a
stack class), plus a Balanced Brackets Checker built on top of it.
"""


class Stack:
    def __init__(self):
        self._data = []

    def push(self, value):
        # Time Complexity: O(1) amortized - append to end of list
        self._data.append(value)

    def pop(self):
        # Time Complexity: O(1) - remove from end of list
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        # Time Complexity: O(1) - look at last element
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


def is_balanced(expression):
    """
    Uses the Stack above to check that (), [], {} are balanced.
    """
    # Time Complexity: O(n) - each character processed once
    pairs = {')': '(', ']': '[', '}': '{'}
    openers = set(pairs.values())
    closers = set(pairs.keys())

    stack = Stack()

    for ch in expression:
        if ch in openers:
            stack.push(ch)
        elif ch in closers:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    print("-- Stack demo --")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("Peek after pop:", s.peek())

    print("\n-- Balanced Brackets Checker --")
    test_cases = [
        "{[a + (b * c)] - [d / e]}",
        "([)]",
        "((a+b)*(c-d))",
        "{[}]",
        "no brackets here",
    ]

    for expr in test_cases:
        result = is_balanced(expr)
        print(f'"{expr}" -> {"Balanced" if result else "Not Balanced"}')
