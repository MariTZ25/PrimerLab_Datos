class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_func(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    #Factor de carga
    def load_factor(self):
        return self.count / self.size
       
    def insert(self, key, value):
        index = self.hash_func(key)
        bucket = self.table[index]

        # manejar colisiones
        found = False
        for idx, element in enumerate(bucket):
            if element[0] == key:
                bucket[idx] = (key, value) # actualizar valor
                found = True
                return
        if not found:
            bucket.append((key, value))  # nuevo
        self.count += 1

        if self.load_factor() > 0.7:
            self.rehash()

    def get(self, key):
        index = self.hash_func(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def rehash(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]

        for bucket in self.table:
            for key, value in bucket:
                index = self.hash_func(key) % new_size
                new_table[index].append((key, value))

        self.size = new_size
        self.table = new_table
    
    def csv_to_hashtable(self, archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    key = linea.split(",")[0]
                    value = linea.split(",")[1].strip()
                    self.insert(key, value)
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado.")
    
    def hashtable_to_csv(self, archivo):
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                for bucket in self.table:
                    for key, value in bucket:
                        f.write(f"{key},{value}\n")
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado.")
    
    def hashtable_to_txtIndex(self, archivo):
        try:
            with open(archivo, "w", encoding="utf-8") as f:
                f.write("Indice | Clave y valor \n")
                f.write("-------------------\n")
                for i, bucket in enumerate(self.table):
                    f.write(f"{i} | {bucket}\n")
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado.")