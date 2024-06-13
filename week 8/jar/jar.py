class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity


    def __str__(self):
        return "🍪" * self.size


    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("exceed capacity")
        self.size += n


    def withdraw(self, n):
        if self.size < n:
            raise ValueError("not enough cookies")
        self.size -= n


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int):
            raise ValueError("capacity is not an integer")
        if int(capacity) < 0:
            raise ValueError("capacity is a negative integer")
        self._capacity = capacity
