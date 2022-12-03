class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distancia(self,puntoA, puntoB):
        return ((puntoA.x - puntoB.x)**2 + (puntoA.y - puntoB.y)**2)**(0.5)
    
    def esOrigen(self):
        if self.x == 0 and self.y == 0:
            return True
        else:
            return False
        
    
    def __str__(self):
        return f"Punto X: {self.x}\nPunto Y: {self.y}"


class poligono:
    def __init__(self, Puntos):
        self.Puntos = Puntos
        
    def perimetro(self):
        per = 0
        for i in range(0,len(self.Puntos)):
            if i+1 == len(self.Puntos):
                per += self.Puntos[0].distancia(self.Puntos[0], self.Puntos[len(self.Puntos)-1])
            else:
                per +=  self.Puntos[0].distancia(self.Puntos[i],self.Puntos[i+1])
        
        return per
    

def main():
    P = Punto(0,0)
    B = Punto(3,4)
    C = Punto(6,0)
    
    poli = poligono([P,B,C])
    print(poli.perimetro())
    

if __name__ == '__main__':
    main()
