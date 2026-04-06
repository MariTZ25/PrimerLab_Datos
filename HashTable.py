class HashTable:
    def _init_(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)] 

    def hash_func(self, key):
        valor = 0
        for i, letra in enumerate(key):
            valor += (i + 1) * ord(letra)
        return valor % self.size

    def insert(self, username, password):
        index = self.hash_func(username)
        password_hash = self.hash_func(password)

        bucket = self.table[index]

        for i, (user, _) in enumerate(bucket):
            if user == username:
                bucket[i] = (username, password_hash)
                return

        bucket.append((username, password_hash))


    def search(self, username, password):
        index = self.hash_func(username)
        password_hash = self.hash_func(password)

        bucket = self.table[index]

        for user, stored_pass in bucket:
            if user == username and stored_pass == password_hash:
                return True
        return False

    def show(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket}")