def Cadena(cad):
    cad2 = ""
    for i in range(0,len(cad)):
        cad2 = cad2 + cad[len(cad)-i-1]
    return cad2

if __name__ == "__main__":
    print(Cadena("XDDDDDD"))