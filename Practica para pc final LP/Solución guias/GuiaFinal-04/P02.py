import math
def EsPrimo(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False        
    return True


def numero(a):
    primo = 0
    n = 0
    resp = 0
    Xd = a
    while a != 0:
        n = int(a%10)
        if EsPrimo(n) == True:
            primo += 1
        a = int(a/10)
    n2 = 0
    while Xd != 0:
        n2 = int(Xd%10) 
        if EsPrimo(n2) == True:
            resp = resp + int(n2*math.pow(10,primo-1))
            primo = primo - 1
        Xd = int(Xd/10)
        
    return resp

        
if __name__ == "__main__":
    print(numero(7417))    