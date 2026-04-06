from HashTable import HashTable
import random as random


hash_table = HashTable()
hash_table.csv_to_hashtable("Repositories/Usuarios.csv")

def generarUsuarios(cantidad):
    for i in range(cantidad):
        user = random_string(random.randint(3, 12))
        if hash_table.get(user) is None:
            password = random_string(8)
            hash_table.insert(user, password)

def random_string(length):
   letters = "|!#$%&/()=?¿¡*+-.@_1234567890qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
   result = ""
   for i in range(length):
       result += random.choice(letters)
   return result

generarUsuarios(20000)
hash_table.hashtable_to_csv("Repositories/Usuarios.csv")
hash_table.hashtable_to_txtIndex("Persistence/IndexStorage/UsuariosIndex.txt")

def imprimir(): 
    print("Indice | Clave y valor \n")
    print("-------------------\n")
    for i, bucket in enumerate(hash_table.table):
        print(f"{i} | {bucket}\n")

#imprimir()

def contar_colisiones(hash_table):
    colisiones = 0
    for bucket in hash_table.table:
        if len(bucket) > 1:
            colisiones += len(bucket) - 1
    return colisiones

print("Número de colisiones:", contar_colisiones(hash_table))

hash_table.insert("prueba", "1234")
print("Factor de carga:", hash_table.load_factor())
print("Valor de 'prueba':", hash_table.get("prueba"))

hash_table.hashtable_to_txtIndex("Persistence/IndexStorage/UsuariosIndex.txt")