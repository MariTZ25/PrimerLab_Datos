class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_func(self, key):
        total = 0
        for i, c in enumerate(key):
            total += (i+1) * ord(c)
        return total % self.size
    
    #Factor de carga
    def load_factor(self):
        return self.count / self.size
       
    def insert(self, key, value):
        index = self.hash_func(key)
        bucket = self.table[index]

        # manejar colisiones
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # reemplaza
                return

        bucket.append((key, value))  # nuevo
        self.count += 1

        if self.load_factor() > 0.7: #nota: existe para que el sistema esté preparado pero probablemnte nunca se exceda el umbral de 0.7
            self.rehash()

    def get(self, key):
        index = self.hash_func(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for k, v in bucket:
                self.insert(k, v)