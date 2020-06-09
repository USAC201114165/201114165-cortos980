carnet = (input('ingrese su carnet: \n'))
dato = 0
lista = []
def secuencia():
    for i in range(carnet):
        if (i % 2==0):
            dato = i
        else:
            dato = (i * 3) + 1
imprimir = lista.append(dato)
print ('la lista queda', str(imprimir))
archivo = open('texto.txt', 'a')
