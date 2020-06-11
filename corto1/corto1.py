carnet = (input('ingrese su carnet: \n'))
dato = 0
lista = []
def secuencia():
    for i in range(carnet):#logica incorrecta para generar secuencia collatz
        if (i % 2==0):
            dato = i
        else:
            dato = (i * 3) + 1
        
imprimir = lista.append(dato) #esto no devuelve nada, .append(), 
print ('la lista queda', str(imprimir))#cambiar imprimir por lista
archivo = open('texto.txt', 'a')

#Funcionamiento:        0/40
#Uso de Funciones       10/20
#Manejo de archivos     5/10
#Manejo de Listas       5/10
#Uso de git             20/20
#*****************************
#Total                  40/100

