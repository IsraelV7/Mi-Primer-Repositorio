from pila import Pila

def invertir_pila(pila):
    if pila.es_vacia():
        print("La pila esta vacia")
        return None
    else:
        pila_aux = Pila()
        contador1 = pila.size()
        while contador1 > 0:
            elemento = pila.pop()
            contador1 -=1
            contador2 = contador1
            while contador2 > 0:
                pila_aux.push(pila.pop())
                contador2 -= 1
            pila.push(elemento)
            while not pila_aux.es_vacia():
                pila.push(pila_aux.pop())

pila1=Pila()
pila1.push(1)
pila1.push(2)
pila1.push(3)
pila1.mostrar()
invertir_pila(pila1)
pila1.mostrar()