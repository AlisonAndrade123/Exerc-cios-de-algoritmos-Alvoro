def calculadora(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."

print(calculadora(10, 5, "+"))
print(calculadora(10, 5, "-"))
print(calculadora(10, 5, "*"))
print(calculadora(10, 5, "/"))
print(calculadora(10, 0, "/"))
print(calculadora(10, 5, "%"))
