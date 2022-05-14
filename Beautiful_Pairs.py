#Creación de la función
def beautifulPairs(A, B):
    cont=0          #Creo la variable contador en 0
    a=sorted(A)     #Ordena las listas A y B
    b=sorted(B)     #de menor a mayor
                                #Se iteran las listas una dentro de la otra para comparar uno a uno 
    for i in range(0, n):       #los elementos en las posiciones de cada lista 
        for j in range(0,n):
            if a[i]==b[j]:      #El condicional evalua si los elementos de la lista a estan en la lista b
                cont+=1         #Si es así se suma un 1 al contador por cada coincidencia dentro de la iteración
                a[i]=0          #Se cambia el elemento de la lista en la posisicoón iterada por un cero para que
                b[j]=0          #no se cuente en la siguiente iteración dentro del condicional
                                #Si el elemento no se encuentra no suma al contador ni se cambia por 0 el elemento
    if cont<n: cont+=1          #Como se debe cambiar un elemento de la lista B se suma o resta un 1 al resultado de cont
    else: cont-=1
    return cont
# Ingreso el tamaño de los arreglos (valor entero) y los Array A y B, con la función map convierto en lista cada elemnto
# y con split elimino los espacio vacios 
n=int(input("Ingrese el tamaño de los Array A y B como un valor entero: "))
A=list(map(int, input("Ingrese el Array de números enteros A separados por espacios: ").split(' ')))
B=list(map(int, input("Ingrese el Array de números enteros B separados por espacios: ").split(' ')))
print("El máximo posible de pares hermosos disjuntos por pares es:")
print(beautifulPairs(A, B))