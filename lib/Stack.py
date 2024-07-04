class Stack:
    def __init__(self, initial_items=None, limit=None):
        if initial_items is None:
            initial_items = []
        self.items = initial_items
        self.limit = limit

    def push(self, item):
        if self.limit is not None and self.size() >= self.limit:
            return
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def full(self):
        if self.limit is None:
            return False
        return self.size() >= self.limit

    def search(self, value):
        try:
            return self.size() - 1 - self.items.index(value)
        except ValueError:
            return -1

    def clear(self):
        self.items = []

    def __str__(self):
        return "Stack: " + str(self.items)