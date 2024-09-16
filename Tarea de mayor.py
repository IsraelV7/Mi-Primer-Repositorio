class COLA:
    def __init__(self, max_size):
        self.max = max_size
        self.cola = [None] * (self.max + 1)
        self.front = 0
        self.back = 0

    def es_vacia(self):
        return self.back == 0 and self.front == 0

    def es_llena(self):
        return self.back == self.max
    
    def size(self):
        return self.back - self.front

    def enqueue(self, elemento):
        if not self.es_llena():
            self.back += 1
            self.cola[self.back] = elemento
        else:
            print("cola llena...")

    def dequeue(self):
        elemento = None
        if not self.es_vacia():
            self.front += 1
            elemento = self.cola[self.front]
            # Si la cola está vacía después de la eliminación
            if self.front == self.back:
                self.front = 0
                self.back = 0
        else:
            print("Cola vacía...")
        return elemento


    def mostrar(self):
        if self.es_vacia():
            print("cola vacia...")
        else:
            print(self.cola[self.front +1: self.back +1])    

    def mayor(self):
        if self.es_vacia():
            return None
        elemento_max = self.cola[self.front + 1]
        for i in range(self.front + 2, self.back + 1):
            if self.cola[i] > elemento_max:
               elemento_max = self.cola[i]
        return elemento_max    

max_size = int(input("Introduce el tamaño maximo de la cola: "))
cola1 = COLA(max_size)

for m in range(max_size):
    if cola1.es_llena():
        print("la cola esta llena")
        break
    elemento = int(input("agregue el elemento: " ))
    cola1.enqueue(elemento)


print("Contenido de la cola")
cola1.mostrar()

cola1.dequeue()
cola1.dequeue()
cola1.dequeue()


print("despues de dequeue")
cola1.mostrar()

mayor1 = cola1.mayor()

print(f"elemento mayor de la cola: {mayor1}")



