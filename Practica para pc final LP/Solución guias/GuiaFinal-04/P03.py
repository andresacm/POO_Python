def picos(l):
    cont = 0
    for i in range(0, len(l)-2):
        if l[i] < l[i+1] > l[i+2]:
            cont += 1
    return cont

if __name__ == "__main__":
    print(picos([0,5,23,14,8,13,3,0]))