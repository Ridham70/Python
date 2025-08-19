class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0 :
            raise ValueError("Number of cookies to deposit must be a non-negative integer")
        if (n + self._size) > self.capacity :
            raise ValueError("Cannot deposite more than the capacity")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0 :
            raise ValueError("Number of cookies to withdraw must be a non-negative integer")
        if n > self._size :
            raise ValueError("Cannot withdraw more than size")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0 :
            raise ValueError("Capacity must be a non-negative integer")
        if capacity < 0 :
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if not isinstance(size, int) or size < 0:
            raise ValueError("Size must be a non-negative integer")
        self._size = size

def main():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()
