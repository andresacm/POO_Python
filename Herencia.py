class Persona:
    
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def FechaNacimiento(self):
        return 2022-self.edad
    
    def __str__(self):
        return f"nombre: {self.nombre}, edad: {self.edad}"
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, codigo):
        self.codigo = codigo
        super().__init__(nombre, edad)
        
    def __str__(self):
        return f"{super().__str__()}, {self.codigo}"
        
        
    
if __name__ == "__main__":
    P1 = Persona("XD", 2)
    print(P1.FechaNacimiento())
    print(P1)
    E1 = Estudiante("RA",4,20)
    print(E1)
    
    