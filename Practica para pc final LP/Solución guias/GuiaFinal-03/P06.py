class HojaCalculo:
    def __init__(self):
        self.filas = []
        #self.columnas = len(self.filas[0])

    def agregarFila(self):
        self.filas.append([])

    def agregarColumna(self):
        for i in self.filas: # Por cada fila le agregamos una celda nula
            i.append(None)

    def verValor(self, fila, columna):
        return self.filas[fila-1][columna-1]

    def asignarValor(self, valor, fila, columna):
        self.filas[fila-1][columna-1] = valor

    def mostrarHoja(self):
        for i in self.filas:
            print(i)

if __name__ == "__main__":
    H = HojaCalculo()
    H.agregarFila()
    H.agregarFila()
    H.mostrarHoja()
    #print(H.verValor(1, 1))
    H.agregarColumna()
    H.agregarColumna()
    H.agregarFila()
    H.mostrarHoja()