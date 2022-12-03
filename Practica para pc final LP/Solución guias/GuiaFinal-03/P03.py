class Cola:
    def __init__(self):
        self.arr = []

    def enqueue(self,e):
        self.arr.append(e)

    def first(self):
        return self.arr[0]
    
    def dequeue(self):
        self.arr.pop(0)

    def __str__(self):
        cad = "ultimo <-- "
        for i in self.arr:
            if i != len(self.arr):
                cad += f"{i} <-- "
            else:
                cad += f"{i} <-- "
        cad += "frente"
        return cad

if __name__ == "__main__":
    C = Cola()
    C.enqueue(1)
    C.enqueue(2)
    C.enqueue(3)
    C.enqueue(4)
    C.enqueue(5)

    print(C)

    