class Lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
            return self.lista
        else:
            print("La lista está llena.")

        def obtener(self,pos):
            if pos < 0 or pos >= self.longitud:
                return None
            else:
                valor = self.lista[pos]
                #listaAux = self.lista[0:pos] + self.lista[pos+1:]
                listaAux = self.lista[0:pos]
                for indice in range(pos,self.longitud-1):
                    listaAux = listaAux + [self.lista[indice+1]]
                self.longitud -= 1
                self.lista = listaAux
                return valor

        def buscar(self,dato):
            pos=1
            if pos:
                return pos
            else:
                return -1

        def insertar(self,dato):
            pass

        def eliminar(self,dato):
            pass

        def mostrar(self,orden="asc"):
            if orden.lower() == "asc":
                for pos in range(0,self.longitud):
                    print("[{}]".format(self.lista[pos]))
            else:
                for pos in range(self.longitud-1,-1,-1):
                    print("[{}]".format(self.lista[pos]))
            
#lista = Lista(4)
#lista.append(3)
#lista.append(4)
#lista.append(2)
#lista.append(8)
#lista.append(9)
#print(lista.obtener(7))
#print(lista.obtener(1))
#lista.mostrar()
#lista.mostrar("des")

