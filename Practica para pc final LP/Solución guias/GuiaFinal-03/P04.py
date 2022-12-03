import P03

class ColaDePrioridad(P03.Cola):
    def __init__(self):
        super().__init__()
    
    def __str__(self):
        self.arr.sort()
        return super().__str__()

if __name__ == "__main__":
    CP = ColaDePrioridad()
    CP.enqueue(2)
    CP.enqueue(1)
    CP.enqueue(6)
    CP.enqueue(7)
    CP.enqueue(0)

    print(CP)