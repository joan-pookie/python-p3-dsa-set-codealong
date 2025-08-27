class MySet:

    def __init__(self, enumerable=[]):
        """Initialize the set with unique values from an iterable."""
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        """Check if a value exists in the set. O(1) runtime."""
        return value in self.dictionary

    def add(self, value):
        """Add a value to the set. O(1) runtime."""
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """Remove a value from the set if it exists. O(1) runtime."""
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """Return the number of elements in the set."""
        return len(self.dictionary)

    def clear(self):
        """Remove all elements from the set."""
        self.dictionary.clear()
        return self

    def __str__(self):
        """Return a human-readable string representation of the set."""
        set_list = [str(key) for key in self.dictionary.keys()]
        return f'MySet: {{{", ".join(set_list)}}}'
