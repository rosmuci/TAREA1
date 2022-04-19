#PROMEDIO
#ENTRADAS
NUM_1=int(input("escribe el 1er número: "))
NUM_2=int(input("escribe el 2do número: "))
NUM_3=int(input("escribe el 3er número: "))
#PROCESOS
SUMA=NUM_1+NUM_2+NUM_3
PROMEDIO=(SUMA/3)
reprobado=(PROMEDIO>6)
aprobado=(PROMEDIO<6)

#SALIDA DE DATOS
print("el promedio es igual a",PROMEDIO)
print("EL PROMEDIO ES ", aprobado)
print("EL PROMEDIO ES ", reprobado)

#AREA Y PERIMETRO
#p=2PI*r   A=PI*R2
#ENTRADAS 
PI=3.1416
r=int(input("escribe el radio del círculo:   "))
#proceso
cuadrado=r**2
Area=PI*cuadrado
Perímetro=(2*PI)*r
#SALIDAS
print("El área del círculo es", Area)
print("El perímetro del círculo es ", Perímetro)

#DETERMINAR LA EDAD DE UNA PERSONA
#ENTRADAS
AÑO_DE_NACIMIENTO = int(input("INGRESA EL AÑO DE NACIMIENTO:  "))
AÑO_DE_ACTUAL = int(input("INGRESA EL AÑO ACTUAL:   "))
#PROCESO
EDAD=AÑO_DE_ACTUAL-AÑO_DE_NACIMIENTO
#SALIDAS
print("La edad es ",EDAD)
#RAIZ CUADRADA
#ENTRADAS
a=int(input("a es igual a:   "))
b=int(input("b es igual a:   "))
c=int(input("c es igual a:   "))
#PROCESO
cuadrado=(b**2)
multiplicación=(4*a*c)
raíz_cuadrada=pow((cuadrado-multiplicación),1/2)
númerador1=((-b)-(raíz_cuadrada))
númerador2=(b-raíz_cuadrada)
denominador=(2*a)
división1=númerador1/denominador
división2=númerador2/denominador
X1=(-(división1))
x2=(división2)
#SALIDAS
print("x1 es igual a ",X1)
print("x2 es igual a ",x2)