class Pila:
    def __init__(self,tamanio=1):
        self.__lista = []
        self.__tope = 0
        self.size = tamanio

    def empty(self):
        return self.__tope == 0
        #self.__size = tamanio
        #if self.tope == 0:
        #    return True
        #else:
        #    return False

        def push(self,dato):
            if self.__tope < self.size:
                self.__lista = self.__lista + [dato]
                self.__tope += 1
            else:
                print("La lista está llena.")

        def pop(self):
            if self.empty():
                return None
            else:
                top = self.__lista[-1]
                self.__tope -= 1
                self.__lista = self.__lista[:-1]
                return top

        def show(self):
            for top in range(self._tope-1,-1,-1):
                print("[{}]".format(self._lista[top]))

        def longitud(self):
            return self.__tope
                

    pila = Pila(4)
    pila.push(4)
    pila.push(6)
    print("Tamaño: {} elementos de {}".format(pila.longitud(),pila.size))
    #print(pila.pop())
    #pila.show()
    #print(pila.pop())
    #pila.show()
    #print(pila.pop())
    #pila.show()
