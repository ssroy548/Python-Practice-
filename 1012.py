A,B,C = input().split()
A,B,C = [float(A),float(B),float(C)]
TRIANGULO = .5*A*C
CIRCULO = 3.14159*C*C
TRAPEZIO = .5*(A+B)*C
QUADRADO = B*B
RETANGULO = A*B
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(TRIANGULO,CIRCULO,TRAPEZIO,QUADRADO,RETANGULO))