
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        total = 0
        for i, c in enumerate(key):
            total += (i+1) * ord(c)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        bucket = self.table[index]

        # manejar colisiones
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # reemplaza
                return

        bucket.append((key, value))  # nuevo

    def get(self, key):
        index = self.hash_func(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

