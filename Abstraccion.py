class Persona:
    
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def FechaNacimiento(self):
        return 2022-self.edad
    
    def __str__(self):
        return f"nombre: {self.nombre}, edad: {self.edad}"
    
if __name__ == "__main__":
    P1 = Persona("XD", 2)
    print(P1.FechaNacimiento())
    print(P1)
    
        
    
    
    