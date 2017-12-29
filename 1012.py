A,B,C = input().split() # taking input inline
A=float(A)
B=float(B)
C=float(C)
pi=3.14159
triangle=A*C/2 # A = base, C = height
circle=pi*C**2 # C = radius (half of diameter)
trapezium=(A+B)*(C/2) # A = bottom length, B = top length, C = vertical height (not the length of the side)
square=B**2 # B = length of one side
rectangle=A*B # A = base, B = height
print("TRIANGULO: %.3f"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapezium)
print("QUADRADO: %.3f"%square)
print("RETANGULO: %.3f"%rectangle)
