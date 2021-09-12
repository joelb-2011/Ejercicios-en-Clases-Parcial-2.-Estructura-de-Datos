class Cola:
    def __init__(self,tamanio=1):
        self.__lista = []
        self.__size=tamanio
        self.__tope=0

    def push(self,dato):
        if self.__tope < self.__size:
            self.__lista = [dato] + self.__lista 
            self.__tope += 1
            return self.__lista
        else:
            print("La lista está llena.")
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.__lista [-1]
            self.__lista = self.__lista [:-1]
            self.__tope -= 1  
            return top
        
    def show(self):
        for top in range (self.__tope):
            print("[{}]".format(self.__lista[top]))
    
    def longitud(self):
        return self.__tope
                    
             
    def empty(self):
        if self.__tope== 0:
            return True
        else:
            return False

#cola1  Cola(3)
#print(cola1.push(8))
#print(cola1.push(10))
#print(cola1.push(12))
#print(cola1.push(4))
#dato = cola1.pop()
