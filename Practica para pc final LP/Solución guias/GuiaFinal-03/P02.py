class Pila:
    def __init__(self):
        self.arr = []

    def push(self,e):
        self.arr.append(e)

    def peek(self):
        return self.arr[len(self.arr)-1]
    
    def pop(self):
        self.arr.pop()

    def __str__(self):
        cad = ""
        for i in self.arr:
            if i != len(self.arr):
                cad += f"{i} <-- "
            else:
                cad += f"{i} <-- "
        cad += "cima"
        return cad

if __name__ == "__main__":
    P = Pila()
    P.push(1)
    P.push(2)
    P.push(3)
    P.push(4)
    P.push(5)

    print(P)

    P.pop()

    print(P)