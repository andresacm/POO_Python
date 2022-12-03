class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Distancia(self,P1, P2):
        return ((P1.x - P2.x)**2 + (P1.y - P2.y)**2)**(0.5)
    
if __name__ == "__main__":
    P1 = Punto(4,5)
    P2 = Punto(3,4)
    P3 = Punto(0,0)
    print(P1.Distancia(P2,P3))
