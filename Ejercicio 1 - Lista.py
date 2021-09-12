from listas import Lista

#lista2 = [2,4,6]

#lista = [[10,20,30],[60,80,90],[25,35,55]]
#print(lista[1],lista[1][1])

#acu=0

#for fila in range(0,len(lista)):
    #print(lista[fila])
    #print(fila,end=" ")
    #acup = 0
    #for col in range(0,len(lista[fila])):
    #    print("[{}]".format(lista[fila][col]),end="")
    #    acu = acu + lista[fila][col]
    #    acup += lista[fila][col]
    #print(acup)
    
#print("Suma Total Elementos: {}".format(acu))

acu=0
lista1 = Lista(3)
for i in range(3):
    dato = input("Ingrese dato")
    lista1.append(dato)
lista1.mostrar()
