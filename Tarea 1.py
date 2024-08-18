#Ordenar una pila de forma descendente de tal manera de que el elemento menor aparesca en el tope de la pila utilizando una pila auxiliar
#El resultado debe mostrarse en la pila original

from pila import Pila

def ordenar_pila(pila):
    if pila.es_vacia():
        print("La pila está vacía")
        return
    
    pila_aux = Pila()
    
    while not pila.es_vacia():
        elemento = pila.pop()

        while not pila_aux.es_vacia() and pila_aux.peek() > elemento:
            pila.push(pila_aux.pop())

        pila_aux.push(elemento)
 
    while not pila_aux.es_vacia():
        pila.push(pila_aux.pop())

pila1 = Pila()
pila1.push(3)
pila1.push(1)
pila1.push(4)
pila1.push(2)

print("Pila original:")
pila1.mostrar()

ordenar_pila(pila1)

print("Pila ordenada:")
pila1.mostrar()
