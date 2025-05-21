A = float(input("Coeficiente A: ").replace(',', '.'))
if A == 0:
    print("\nNão é equação do 2º grau.")
    exit(1)
B = float(input("Coeficiente B: ").replace(',', '.'))
C = float(input("Coeficiente C: ").replace(',', '.'))

delta = B**2 - 4*A*C

if delta > 0:
    raiz1 = (-B + (delta ** 0.5)) / (2 * A)
    raiz2 = (-B - (delta ** 0.5)) / (2 * A)
    print(f"x1 = {raiz1:.4f}")
    print(f"x2 = {raiz2:.4f}")

elif delta == 0:
    raiz = -B / (2 * A)
    print(f"x = {raiz:.4f}")

else:
    parte_real = -B / (2 * A)
    parte_imag = (abs(delta) ** 0.5) / (2 * A)
    print(f"x1 = {parte_real:.4f} + {parte_imag:.4f}i")
    print(f"x2 = {parte_real:.4f} - {parte_imag:.4f}i")
