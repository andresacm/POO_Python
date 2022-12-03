def MenorPromedioMayor(arr):
    lista = []
    lista.append(arr[0])
    lista.append(arr[1])
    sum = 0
    for i in arr:
        if i >= lista[0]:
            lista[0] = i
        elif i <= lista[1]:
            lista[1] = i
        sum += i
    sum = round(sum/len(arr),2)
    lista.append(sum)
    
    return lista

if __name__ == "__main__":
    arr = [5,7,15,2,0,4,6]
    print(MenorPromedioMayor(arr))