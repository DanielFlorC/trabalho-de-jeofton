# criando o historico
historico = []

# dando as opções 
while True:
  print("Digite uma opção abaixo")
  print("1- CALCULADORA NORMAL")
  print("2- CONVERTER TEMPERATURA")
  print("3- CALCULADORA DE IMC")
  print("4- FINALIZAR CODIGO")
  escolha= input("DIGITE SUA ESCOLHA:")

# parte da calculadora
  if escolha == '1':
    print("1- FAZER UMA CONTA:")
    print("2- VER O HISTORICO:")
    escolha_2 = input("DIGITE SUA ESCOLHA:")
    if escolha_2 == '1':
      numero1 = float(input("DIGITE UM NUMERO:"))
      operador = input("DIGITE UM OPERADOR:")
      numero2 = float(input("DIGITE UM NUMERO:"))
      if operador == "+":
        resultado = numero1 + numero2
      elif operador == "-":
        resultado = numero1 - numero2
      elif operador == "*":
        resultado = numero1 * numero2
      elif operador == "/":
          if numero2 != "0":
            resultado = numero1 / numero2
          else:
            print("ERRO DIVISÃO POR ZERO!")
            continue
      if operador == "**":
        resultado = numero1 ** numero2
      print ("O resultado da sua operação é -->",resultado)
      # adicionando resultado ao historico
      historico.append(f"{numero1} {operador} {numero1} = {resultado}")
    
    # mostrando o historico
    if escolha_2 == "2":
      print(historico)