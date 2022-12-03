class Triangulov2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.perimetro = self.a + self.b + self.c
        S = (self.a+self.b+self.c)/2
        self.area = (S*(S-self.a)*(S-self.b)*(S-self.c))**(1/2)
    
    def Perimetro(self):
        return self.perimetro
    
    def Area(self):
        return self.area
    
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
    T = Triangulov2(4,6,8)
    print(T)
    
    