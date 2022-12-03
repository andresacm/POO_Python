import P03
class LazyColaDePrioridad(P03.Cola):
    
    def dequeue(self):
        super().dequeue()
        self.arr.sort()

    
    def __str__(self):
        self.arr.sort()
        return super().__str__()

if __name__ == "__main__":
    LCP = LazyColaDePrioridad()

    LCP.enqueue(0)
    LCP.enqueue(5)
    LCP.enqueue(1)
    LCP.enqueue(2)

    print(LCP)