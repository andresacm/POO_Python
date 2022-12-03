class monomio:
    def __init__(self, coef, expt):
        self.coef = coef
        self.expt = expt
    def evaluar(self, v):
        return self.coef * v**self.expt
    def imp(self):
        ans = ""
        ans += str(self.coef) + "x"+"^"+ str(self.expt)+"+"
        return ans
    
class polinomio():
    def __init__(self, monomios):
        self.monomios = monomios
    def agregarP(self, new):
        self.monomios.append(new)
    def evaluar(self, v):
        ans = 0
        for i in self.monomios:
            ans += i.evaluar(v)
        return ans
    def mostrar(self):
        ans = ""
        for i in self.monomios:
            ans += i.imp()
        return ans

def main():
    
    A = monomio(2,2)
    B = monomio(5,1)
    
    
    
    pol = polinomio([A,B])
    print(pol.mostrar())
    pol.agregarP(monomio(3,5))
    
    print(pol.mostrar())
    print(pol.evaluar(1))
    
    
main()
