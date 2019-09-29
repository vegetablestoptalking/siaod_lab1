from LinkedList import List as ls


class Stack:
    def __init__(self):
        self.val = ls()

    def push(self, value):
        self.val.append(value)

    def pop(self):
        return self.val.pop()

    def __str__(self):
        return self.val.__str__()

    def __len__(self):
        return self.val.length()

    def __getitem__(self, key):
        return self.val.__getitem__(key)
