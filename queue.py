

# Chapter 8: Queues

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
queue.enqueue(10)
queue.enqueue(20)
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
