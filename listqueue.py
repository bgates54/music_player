"""
File: listqueue.py
Author: Vincent Arcuri
A list-based implementation of stacks.
"""

class ListQueue(object):

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = []
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        if len(self) == 0:
            return True
        else:
            return False
    
    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the queue."""
        return "{" + ', '.join(map(str, self.items)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        new_queue = ListQueue(sourceCollection=self.items)
        for item in other:
            new_queue.add(item)
        return new_queue

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if type(other) == type(self) and len(self) == len(other):
            for this, that in zip(self, other):
                if this != that:
                    break
            else:
                return True
        return False


    def peek(self):
        """Returns the item at the front of the queue.
        Raises IndexError if queue is not empty."""
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            return self.items[0]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = []

    def add(self, item):
        """Inserts item at the rear of the queue."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at the front of the
        queue. Raises IndexError if queue is not empty."""
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            popped_item = self.items.pop(0)
            return popped_item

