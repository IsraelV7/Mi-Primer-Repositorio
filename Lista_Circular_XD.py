class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None

class lista_circular:
    def __init__(self):
        self.p = None
    
    def es_vacia(self):
        return self.p is None
    
    def agregar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.es_vacia():
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p
            print("Se agregó un nuevo nodo:", valor)
        else:
            actual = self.p
            print("Agregando nodo al final:", valor)
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.p    

    def agregar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.es_vacia():
            self.p = nuevo_nodo
            nuevo_nodo.siguiente = self.p
            print("Se agregó un nuevo nodo al inicio:", valor)
        else:
            nuevo_nodo.siguiente = self.p
            actual = self.p
            while actual.siguiente != self.p:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.p = nuevo_nodo
            print("Se agregó un nuevo nodo al inicio:", valor)

    def eliminar_final(self):
        if self.es_vacia():
            print("La lista circular está vacía. No se puede eliminar.")
            return
        
        if self.p.siguiente == self.p:  # Solo hay un nodo
            print("Eliminando nodo:", self.p.elemento)
            self.p = None
            return
        
        actual = self.p
        while actual.siguiente.siguiente != self.p:
            actual = actual.siguiente
        print("Eliminando nodo:", actual.siguiente.elemento)
        actual.siguiente = self.p  

    def eliminar_inicio(self):
        if self.es_vacia():
            print("La lista circular está vacía. No se puede eliminar.")
            return
        
        if self.p.siguiente == self.p:  
            print("Eliminando nodo:", self.p.elemento)
            self.p = None
            return
        
        print("Eliminando nodo:", self.p.elemento)
        actual = self.p
        while actual.siguiente != self.p:
            actual = actual.siguiente
        self.p = self.p.siguiente  
        actual.siguiente = self.p  

    def mostrar(self):
        if self.es_vacia():
            print("La lista circular está vacía...")
            return
        
        actual = self.p
        output = []
        while True:
            output.append(actual.elemento)
            actual = actual.siguiente
            if actual == self.p:
                break
        output.append("(inicio)")
        print(" -> ".join(output))

listaC1 = lista_circular()
listaC1.agregar_final("ana")
listaC1.agregar_final("pedro")
listaC1.agregar_inicio("maria")
listaC1.mostrar()

listaC1.eliminar_final()
listaC1.mostrar()

listaC1.eliminar_inicio()
listaC1.mostrar()
