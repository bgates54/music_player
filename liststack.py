"""
File: liststack.py
Author: Vincent Arcuri
A list-based implementation of stacks.
"""


class ListStack(object):
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = []
        if sourceCollection:
            for item in sourceCollection:
                self.items.append(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if the stack is empty, or False otherwise."""
        if len(self) == 0:
            return True
        else:
            return False
    
    def __len__(self):
        """Returns the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Returns the string representation of the stack."""
        return "{" + ", ".join(map(str, self.items)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the stack."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1


    def __add__(self, other):
        """Returns a new stack containing the contents
        of self and other."""
        new_items = [] + self.items
        for i in other:
            new_items.append(i)
        return ListStack(sourceCollection=new_items)


    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if len(self) == len(other) and type(self) == type(other):
            for i, j in zip(self, other):
                if i != j:
                    break
            else:
                return True
        return False

    def peek(self):
        """Returns the item at top of the stack.
        Raises IndexError if stack is empty."""
        if not self.isEmpty():
            return self.items[len(self) - 1]
        else:
            raise IndexError("Stack is empty")

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = []

    def push(self, item):
        """Inserts item at the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item at top of the stack.
        Raises IndexError if stack is empty."""
        if self.isEmpty():
            raise IndexError("Stack is empty")
        else:
            removed_item = self.items.pop()
            return removed_item

