class Auto:
    def __init__(self):
        self.color = 'rojo'
        self.marca = 'peta'
        self.modelo = 2000

    def mostrar(self):
        print(self.color, self.marca, self.modelo)
           
    def leer(self):
        self.color = input('Ingresar el color del auto:  ')
        self.marca = input('Ingrese la marca del auto:  ')       
        self.modelo = input('Ingrese el modelo del auto:  ')

carro1 = Auto()
carro1.mostrar()       