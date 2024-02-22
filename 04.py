numeros=[12,22,23,34,35,36,77,88]
impar=[]

total = len(numeros)

for x in range(total):
    if (numeros[x] %2 == 0):
        print(numeros[x])
    
    else:
     
        impar.append(numeros[x])
 
 
print(impar)
 