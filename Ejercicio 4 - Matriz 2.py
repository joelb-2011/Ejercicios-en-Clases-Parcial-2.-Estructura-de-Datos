import os
class Matriz:
    def __init__(self,nfilas,ncols):
        self.matriz = []
        self.noFilas = nfilas
        self.noCols = ncols

    def ingresar(self):
        os.system("cls")
        self.matriz = []
        for fila in range(self.noFilas):
            columnas = []
            for col in range(self.noCols):
                valor = int(input("Fila[{}] Col[{}]: ".format(fila,col)))
                columnas.append(valor)
            self.matriz.append(columnas)

    def mostrar(self):

        print("-----------------")
        for fila in range(len(self.matriz)):
            #print(self.matriz[fila])
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()
        print("-----------------")

    def buscar(self,buscado):
        resp = {} 
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col] == buscado:
                    resp["fila"]=fila
                    resp["col"]=col
                    break
            if resp: break
        return resp

    def buscarW(self,buscado):
        resp = {}
        fila=0
        enc=False
        while fila < len(self.matriz) and enc==False:
            col=0
            while col < len(self.matriz[fila]) and enc==False:
                if self.matriz[fila][col] == buscado:
                    resp["fila"]=fila
                    resp["col"]=col
                    enc=True
                else: col += 1
            fila += 1
        return resp

    def sumar(self,mat2):
        matrizSuma = []
        for fila in range(self.noFilas):
            columnas = []
            for col in range(self.noCols):
                valor = self.matriz[fila][col] + mat2[fila][col]
                columnas.append(valor)
            matrizSuma.append(columnas)
        return matrizSuma

    #numeros = [[11,20,15],[10,25,30],[11,25,31]]

    numeros = []
    mat1 = Matriz(2,2)
    mat1.ingresar()
    mat2 = Matriz(2,2)
    mat2.ingresar()
    mat1.mostrar()
    mat2.mostrar()
    mat2.matriz = mat2.sumar(mat1.matriz)
    mat1.mostrar()
    
    #resp = mat.buscarW(25)
    #if resp: print(resp)
    #else: print("dato no encontrado")
