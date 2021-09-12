class Busqueda:

    def __init__(self,listas=None):
        self.__lista=listas

    @property
    def lista (self): #getProperty()
        if self.__lista != None:
            return self.__lista
        else:
            print("Lista Vacia.")

    #busca un dato en una lista
    def busquedaLineal(self,buscado):
        lon = len(self.__lista)
        enc=False
        pos=0
        #recorrer la lista hasta que encontrar al dato buscado
        #o pos sea igual a la longitud de la lista lo cual
        #indica que el dato no fue encontrado
        while pos < lon and enc==False:
            if self.__lista[pos]["nombre"] == buscado: enc=True
            else: pos += 1
        if enc: return pos
        else: return -1

    def ordenar(self,orden):
        if orden == "asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self._lista[pos]["nombre"] > self._lista[sig]["nombre"]:
                        aux = self.__lista[pos]
                        self._lista[pos]=self._lista[sig]
                        self.__lista[sig]=aux
        else:
            if orden =="des":
                for pos in range(0,len(self.__lista)):
                    for sig in range(pos+1,len(self.__lista)):
                        if self._lista[pos]["nombre"] < self._lista[sig]["nombre"]:
                            aux = self.__lista[pos]
                            self._lista[pos]=self._lista[sig]
                            self.__lista[sig]=aux

    def busquedaBinaria(self,buscado):
        pass

    notas = [
        {"nombre":"Daniel", "n1":20, "n2": 40},
        {"nombre":"Danny", "n1":30, "n2": 50},
        {"nombre":"Dayana", "n1":40, "n2": 50},
        {"nombre":"Erick", "n1":50, "n2": 40},
        {"nombre":"Romina", "n1":55, "n2": 40},
        {"nombre":"Yady", "n1":60, "n2": 40}
    ]

    print(notas[3])
    bus1 = Busqueda(notas)
    #print(bus1.busquedaLineal("erick"))
    bus1.ordenar("des")
    print(bus.lista)
    
