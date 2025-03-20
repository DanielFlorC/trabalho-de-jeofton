hitorico = []

while True:
  print("Digite uma opção abaixo")
  print("1- CALCULADORA NORMAL")
  print("2- CONVERTER TEMPERATURA")
  print("3- CALCULADORA DE IMC")
  print("4- FINALIZAR CODIGO")
  escolha= input("DIGITE SUA ESCOLHA:")

  if escolha == '1':
    numero1 = float(input("DIGITE UM NUMERO:"))
    operador = input("DIGITE UM OPERADOR:")
    numero2 = float(input("DIGITE UM NUMERO:"))
    if operador == "+":
      resultado = numero1 + numero2
    if operador == "-":
      resultado = numero1 - numero2
    if operador == "*":
      resultado = numero1 * numero2
    if operador == "/":
      resultado = numero1 / numero2
    if operador == "**":
      resultado = numero1 ** numero2
    print ("O resultado da sua operação é -->",resultado)

