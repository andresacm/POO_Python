class Persona:
    
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def FechaNacimiento(self):
        return 2022-self.__edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
    
    def __str__(self):
        return f"nombre: {self.__nombre}, edad: {self.__edad}"
    
if __name__ == "__main__":
    P1 = Persona("XD", 2)
    print(P1.FechaNacimiento())
    print(P1)
    