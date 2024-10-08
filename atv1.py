# Início do código: vamos pedir ao usuário seu peso e sua altura
# Sempre que precisamos de dados do usuário, usamos a função input()

# Recebe o peso da pessoa. Usamos float porque o peso pode ser decimal (ex: 70.5 kg)
peso = float(input("Digite o seu peso em kg: "))

# Recebe a altura da pessoa. Também pode ser decimal (ex: 1.75 metros)
altura = float(input("Digite a sua altura em metros: "))

# Agora, vamos calcular o IMC usando a fórmula que vimos antes
# IMC = peso / (altura * altura)
imc = peso / (altura ** 2)

# Usando f-string para formatar a saída: uma f-string é uma forma de combinar texto
# com variáveis de maneira clara e direta.
# O código {imc:.2f} dentro da f-string garante que o IMC será exibido com 2 casas decimais
print(f"Seu IMC é: {imc:.2f}")

# Agora, vamos classificar o IMC usando estruturas condicionais (if, elif, else)

# Se o IMC for menor que 18.5, a pessoa está abaixo do peso
if imc < 18.5:
    print("Você está abaixo do peso.")

# Se o IMC for entre 18.5 e 24.9, é considerado peso normal
elif imc >= 18.5 and imc <= 24.9:
    print("Você está com o peso normal.")

# Se o IMC for entre 25.0 e 29.9, é considerado sobrepeso
elif imc >= 25.0 and imc <= 29.9:
    print("Você está com sobrepeso.")

# Se o IMC for 30.0 ou maior, a pessoa é considerada obesa
else:
    print("Você está com obesidade.")
