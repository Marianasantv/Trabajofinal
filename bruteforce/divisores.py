def divisores(n):
    ndivisores = []
    num = n
    for i in range (1, n+1):
        if (num%i == 0):
            ndivisores.append(i)
    return ndivisores
x = 20
result = (divisores(x))
print("N es: "+ str(x)+ " Sus divisores son: " + str(result))