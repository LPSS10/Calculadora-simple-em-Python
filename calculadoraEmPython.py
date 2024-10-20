

print('-------------------------------------------')
print("# Desenvolvendo uma calculadora em Python com funções")
print('-------------------------------------------')

def soma(numeros):
    return int(numeros[0]) + int(numeros[1])

def divisao(numeros):
    return int(numeros[0]) / int(numeros[1])

def subtracao(numeros):
    return int(numeros[0]) - int(numeros[1])

def multiplicacao(numeros):
    return int(numeros[0]) - int(numeros[1])

numeros_input = input('Digite os números separados por espaço: ').split(' ')
print('-------------------------------------------')

operacao_input = input('Digite a operação(+ - / *): ')
print('-------------------------------------------')

resultado_calculo = 0

if len(numeros_input) !=2:
    print('Quantidade de números de entrada diferente de 2') # Controle de numeros de entrada
else:
   if operacao_input in '+-/*':
    if operacao_input == '+':
           resultado_calculo =soma(numeros_input)

    elif operacao_input == '-':
            resultado_calculo = subtracao(numeros_input)

    elif operacao_input == '/':
       resultado_calculo = divisao(numeros_input)

    elif operacao_input == '*':
       resultado_calculo = multiplicacao(numeros_input)

    print(f'Resultado da operação é: {resultado_calculo}')
   else:
    print(f'Operação {operacao_input} invalida')