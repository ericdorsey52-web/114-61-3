# data_structures.py
# This file contains implementations of basic data structures: Stack and Queue.
# These are implemented using Python lists for simplicity and beginner-friendliness.

class Stack:
    """
    A simple Stack implementation using a Python list.
    Supports basic stack operations: push, pop, peek, is_empty, size.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item from the stack without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

# Example usage for Stack:
# stack = Stack()
# stack.push(1)
# stack.push(2)
# print(stack.peek())  # Output: 2
# print(stack.pop())   # Output: 2
# print(stack.size())  # Output: 1

class Queue:
    """
    A simple Queue implementation using a Python list.
    Supports basic queue operations: enqueue, dequeue, is_empty, size.
    """
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def is_empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item from the queue. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

# Example usage for Queue:
# queue = Queue()
# queue.enqueue('a')
# queue.enqueue('b')
# print(queue.dequeue())  # Output: 'a'
# print(queue.size())     # Output: 1