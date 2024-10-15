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

    def mayor_caracter(self):
        if self.es_vacia():
            return None

        mayor = self.P.elemento
        actual = self.P.siguiente
        while actual:
            if actual.elemento > mayor:
                mayor = actual.elemento
            actual = actual.siguiente
        return mayor

    def unir_y_ordenar(self, otra_lista):
        elementos = []
        actual = self.P
        while actual:
            elementos.append(actual.elemento)
            actual = actual.siguiente

        actual = otra_lista.P
        while actual:
            elementos.append(actual.elemento)
            actual = actual.siguiente

        elementos.sort()

        lista_ordenada = Lista()
        for elemento in elementos:
            lista_ordenada.adicionar_final(elemento)
        
        return lista_ordenada

lista1 = Lista()
lista2 = Lista()

lista1.adicionar_final('b')
lista1.adicionar_final('a')
lista1.adicionar_final('c')

lista2.adicionar_final('e')
lista2.adicionar_final('d')
lista2.adicionar_final('f')

mayor_lista1 = lista1.mayor_caracter()
mayor_lista2 = lista2.mayor_caracter()

if mayor_lista1 > mayor_lista2:
    print("La lista 1 tiene el mayor carácter:", mayor_lista1)
    print("Contenido de la lista 1:")
    lista1.mostrar()
else:
    print("La lista 2 tiene el mayor carácter:", mayor_lista2)
    print("Contenido de la lista 2:")
    lista2.mostrar()

lista_unida = lista1.unir_y_ordenar(lista2)
print("Lista unida y ordenada:")
lista_unida.mostrar()
