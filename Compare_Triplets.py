#Creación de la función
def compareTriplets(a, b):
    alice = []                              #Creación listas vacias
    bob = []
                                            #Se iteran las tripeltas para comparar uno a uno los elementos
    for i in range(len(a)):                 #en la misma posición de cada tupla
        if(a[i] > b[i]): alice.append(1)    #Si a>b en la posición i se agrega un 1 a la lista alice 
        elif(a[i] < b[i]): bob.append(1)    #Si a<b en la posición i se agrega un 1 a la lista bob
        else: continue                      #Si no cumplen las condiciones sale del condicional if
    return sum(alice), sum(bob)             #Se retorna la suma de los elementos de cada lista
#Ingreso las tripletas de los argumento a y b, con la función map convierto en tupla cada elemnto y con split elimino los espacio vacios 
a=tuple(map(int, input("Ingrese los 3 valores de la calificación de Alice separados por espacios: ").split(' ')))   
b=tuple(map(int, input("Ingrese los 3 valores de la calificación de Bob separados por espacios: ").split(' ')))   
print("Las calificaciónes de Alice y Bob respectivamente son:")
print(compareTriplets(a, b))                #Invoca la función