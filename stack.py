# Chapter 7: Stacks

## Implementation of a Stack Using a List
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())


## Matching Parentheses Example
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

print(is_balanced("{[()]}"))  # Output: True
print(is_balanced("{[(])}"))  # Output: False


## Convert Infix to Postfix
def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = Stack()

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char in precedence:
            while not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[char]:
                output.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('

    while not stack.is_empty():
        output.append(stack.pop())

    return ''.join(output)


print(infix_to_postfix("A*(B+C)"))  # Output: ABC+*