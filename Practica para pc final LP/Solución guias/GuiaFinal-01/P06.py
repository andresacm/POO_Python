class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def Perimetro(self):
        return self.a+self.b+self.c
    
    def Area(self):
        S = (self.a+self.b+self.c)/2
        return (S*(S-self.a)*(S-self.b)*(S-self.c))**(1/2)
    
    def Tipo(self):
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a != self.b != self.c:
            return "Escaleno"
        else:
            return "isóceles"
    
    def __str__(self):
        return f"Lado a: {self.a} \nLado b: {self.b} \nLado c: {self.c}"
    
if __name__ == "__main__":
    T = Triangulo(4,6,8)
    print(T)
    
    