class Persona:
    def __init__(self, codigo, nombre, direccion):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return f"Codigo: {self.codigo}\nNombre: {self.nombre}\nDireccion: {self.direccion}"
    
class Alumno(Persona):
    def __init__(self, codigo, nombre, direccion, departamento, ciclo):
        self.departamento = departamento
        self.ciclo = ciclo
        super().__init__(codigo, nombre, direccion)

    def estudiar(self):
        print("Estoy webeando")

    def rendExamen(self):
        print("Jale LP")

    def __str__(self):
        return f"{super().__str__()}\ndepartamento: {self.departamento}\nciclo: {self.ciclo}"

class Docente(Persona):
    def __init__(self, codigo, nombre, direccion, escuelaprofesional, salariomensual):
        self.escuelaprofesional = escuelaprofesional
        self.salariomensual = salariomensual 
        super().__init__(codigo, nombre, direccion)
    
    def dictar(self):
        print("dictanding")

    def corregirExamen(self):
        print("Salao p")
    
    def __str__(self):
        return f"{super().__str__()}\nEscuela: {self.escuelaprofesional}\nSalario: {self.salariomensual}"

if __name__ == "__main__":
    P = Persona(21, "XD", "raaa123")
    A = Alumno(45, "XDn't", "gaa12", "asd", 0)
    D = Docente(78, "DX", "ewrdf", "a", 0)
    print(P)
    print(A)
    print(D)

