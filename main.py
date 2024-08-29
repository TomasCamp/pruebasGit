from src import calculator

def main():
    num1 = float(input("Escriba el primer número: "))
    num2 = float(input("Escriba el segundo número: "))
    operator = input("Escriba el el oeperador (+, -, *, /): ")
    result = calculator.calculate(num1, num2, operator)
    print(f"El resultado es: {result}")

if __name__ == "__main__":
    main()