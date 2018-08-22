x=float(input("Escribe un numero: "))
if x%5==0:
    print(x, " es multiplo de 5.")
else:
    print(x, " no es multiplo de 5.")

x=int(input("Esctibe tu edad: "))
y=input("Tienes INE? (si/no) ")
if x>=18 and y=="si":
    print("¡Si puede votar!")
else:
    print("Lo siento, no puede votar.")
    
