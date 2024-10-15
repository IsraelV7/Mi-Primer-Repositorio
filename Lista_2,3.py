class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None

class Lista:
    def __init__(self):
        self.P = None

    def es_vacia(self):
        return self.P is None 

    def adicionar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.P is None:
            self.P = nuevo_nodo
        else:
            actual = self.P
            while actual.siguiente: 
                actual = actual.siguiente     
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.P
        while actual:
            print(actual.elemento, end=" -> ")
            actual = actual.siguiente
        print("None")           

    def eliminar_multiples_de_2(self):
        actual = self.P
        anterior = None
        while actual:
            if actual.elemento % 2 == 0:  
                if anterior is None:  
                    self.P = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
            else:
                anterior = actual
            actual = actual.siguiente

lista1 = Lista()

lista1.adicionar_final(3)
lista1.adicionar_final(6)
lista1.adicionar_final(9)
lista1.adicionar_final(12)
lista1.adicionar_final(15)
lista1.adicionar_final(18)
lista1.adicionar_final(21)
lista1.adicionar_final(24)
lista1.adicionar_final(27)
lista1.adicionar_final(30)

print("Lista original de múltiplos de 3:")
lista1.mostrar()

lista1.eliminar_multiples_de_2()
print("Lista después de eliminar múltiplos de 2:")
lista1.mostrar()