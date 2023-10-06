class Calculadora:
    def __init__(self):
        self.numero1 = int(input("Ingrese el primer número entero: "))
        self.numero2 = int(input("Ingrese el segundo número entero: "))

    def suma(self):
        resultado = self.numero1 + self.numero2
        return resultado

    def resta(self):
        resultado = self.numero1 - self.numero2
        return resultado

    def multiplicacion(self):
        resultado = self.numero1 * self.numero2
        return resultado

    def division(self):
        if self.numero2 != 0:
            resultado = self.numero1 / self.numero2
            return resultado
        else:
            return "No se puede dividir por cero."

# Crear una instancia de la clase Calculadora
mi_calculadora = Calculadora()

# Calcular y mostrar los resultados
print(f"Suma: {mi_calculadora.suma()}")
print(f"Resta: {mi_calculadora.resta()}")
print(f"Multiplicación: {mi_calculadora.multiplicacion()}")

# Verificar si se puede realizar la división antes de llamar al método
if mi_calculadora.numero2 != 0:
    print(f"División: {mi_calculadora.division()}")
else:
    print(mi_calculadora.division())
