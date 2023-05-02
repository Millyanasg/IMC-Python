altura = float(input("Informe a sua altura em metros: "))
peso = float(input("Informe o seu peso em quilos: "))

imc = peso / (altura ** 2)

print("Seu IMC é: {:.2f}".format(imc))