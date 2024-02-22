numeros[5,-3,10,8,-2,15,7,-9,4,6]
menos=0
mais=0

total=len(numeros)

for x in range(total):
    
    
     if(numeros[x]<0):
         menos=menos+1
         print(numeros[x])
         
     else:
        mais=mais+1
        print(numeros[x])
         
    
    
    
    
print("quantidade de positivo",mais)
print("quantidade de negativos",menos)  