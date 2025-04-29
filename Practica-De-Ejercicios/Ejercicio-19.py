pares=[]

for i in range(5):
    numero=int(input(f"ingresa el numero{i+1}:"))
    if numero %2 ==0:
        pares.append(numero)
    
print("los numeros pares son:", pares)