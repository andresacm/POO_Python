class Lista:
    def __init__(self):
        self.arr = []

    def agregarElemento(self,e,i):
        self.arr.insert(i,e)

    def eliminarElemento(self,i):
        self.arr.pop(i)
    
    def verValor(self, i):
        return self.arr[i-1]

    def cantidadElementos(self):
        return len(self.arr)
    
    def __str__(self):
        cad = ""
        for i in self.arr:
            cad += f"{i} --> "
        cad += "null"
        return cad

if __name__ == "__main__":
    L = Lista()
    L.agregarElemento(1,1)
    L.agregarElemento(2,2)
    L.agregarElemento(3,3)
    L.agregarElemento(4,4)

    print(L)