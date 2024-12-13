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
stack.push(15)
stack.push(30)
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

## Implementation of a Queue Using a List
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


queue = Queue()
queue.enqueue(8)
queue.enqueue(19)
print(queue.dequeue())


## Simulation Example (Customer Queue)
import random

def simulate_checkout(customers, service_time):
    queue = Queue()
    total_wait_time = 0

    for customer in customers:
        queue.enqueue(customer)
        total_wait_time += service_time

    while not queue.is_empty():
        print(f"Serving customer: {queue.dequeue()}")

    print(f"Total wait time: {total_wait_time} minutes")

customers = ["Alice", "Bob", "Charlie", "Diana"]
simulate_checkout(customers, service_time=5)
