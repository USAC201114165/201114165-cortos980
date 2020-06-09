carnet = (input('ingrese su carnet: \n'))
lista = []
def secuencia():
    for i in range(carnet):
        if (i % 2==0):
            dato = i
        else (i % 2!=0):
            dato = (i * 3) + 1
imprimir = lista.append(dato)
print ('la lista queda', str(imprimir))
archivo = open('texto', 'a')
