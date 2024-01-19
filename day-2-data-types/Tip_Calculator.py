print("Bem vindo a Calculadora de Gorjetas!")
conta_total = input("Qual foi o total da conta? R$:")
porcentagem = input("Que porcentagem você gostaria de pagar? 10, 12 ou 15? ")
numero_pessoas = input("Quantas pessoas vão dividir a conta? ")

porcentagem_gorjeta = float(conta_total) * (int(porcentagem)/100)
gorjeta = (float(conta_total)+ porcentagem_gorjeta)/int(numero_pessoas)

print("Cada pessoa deve pagar: R$" + str(round(gorjeta, 2)))