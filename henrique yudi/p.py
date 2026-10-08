# 1 - CRIE UM PROGRAMA QUE PARA CALCULAR O IMC DO USUÁRIO
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / altura ** 2

print(f"Seu imc é {imc} ")
# 2 - CRIE UM PROGRAMA QUE PEÇA UM NOME E UMA IDADE E MOSTRE A FRASE: "OLÁ, _______. DAQUI A 10 ANOS VOCÊ TERÁ X ANOS"
nome = (input("Digite seu nome: "))
idade = float(input("Digite sua idade: "))
idadedez = idade + 10 

print(f"OLÁ, {nome} DAQUI A 10 ANOS VOCÊ TERÁ {idadedez} anos")

# 3 - FAÇA UM PROGRAMA QUE PEÇA UMA TEMPERATURA EM CELSIUS E CONVERTA PARA FAHRENHEIT (F = C * 9/5 + 32)
celsius = float(input("Digite os graus celsius da temperatura "))
fahrenheit = celsius * 9/5 + 32

print(f"a temperatura em fahrenheit é {fahrenheit}")
# 4 - FAÇA UM PROGRAMA QUE PEÇA 3 NOTAS E FAÇA A MÉDIA.
nota1 = float(input("Digite sua nota no 1 trimestre: "))
nota2 = float(input("Digite sua nota no 2 trimestre: "))
nota3 = float(input("Digite sua nota no 3 trimestre: "))
media = (nota1 + nota2 + nota3) / 3

print(f"Sua media é{media}")
# 5 - FAÇA UM PROGRAMA QUE PEÇA A BASE E A ALTURA DE UM RETÂNGULO E MOSTRE A ÁREA E O PERÍMETRO.
base = float(input("Digite a base do triangulo: "))
altura = float(input("Digite a altura do triangulo: "))
area = base * altura
perimetro = base * 2 + altura * 2

print(f"{area} {perimetro}")
# 6 MELHORE O PROGRAMA DE IMC CRIANDO CONDIÇÕES PARA:
nome = input('Qual seu nome? ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'{nome}, seu IMC é: {imc:.2f} e você está abaixo do peso')

elif imc >=18.5 and imc <= 24.9:
    print(f'{nome}, seu IMC é: {imc:.2f} e você está no peso normal(saudavel)')

elif imc >=25.0 and imc <= 29.9:
    print(f'{nome}, seu IMC é: {imc:.2f} e você está sobrepeso')

elif imc >=30.0 and imc <= 34.9:
    print(f'{nome}, seu IMC é: {imc:.2f} e você está na obesidade grau 1')

elif imc >=35.0 and imc <= 39.9:
    print(f'{nome}, seu IMC é: {imc:.2f} e você está na obesidade grau 2')

else :
    print(f'{nome}, seu IMC é: {imc:.2f} e você está na obesidade grau 3')
    
    
#Menor que 18,5	Magreza / Abaixo do peso
#Entre 18,5 e 24,9	Peso normal (saudável)
#Entre 25,0 e 29,9	Sobrepeso
#Entre 30,0 e 34,9	Obesidade Grau I
#Entre 35,0 e 39,9	Obesidade Grau II
#Maior ou igual a 40,0	Obesidade Grau III (Grave)
