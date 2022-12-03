def sumDivisores(a):
    suma = 0
    for i in range(1,a):
        if a%i == 0:
            suma += i
    return suma

def Hermanos(n1,n2):
    return sumDivisores(n1) == n2 and sumDivisores(n2) == n1
    
if __name__ == "__main__":
    print(Hermanos(220,284))