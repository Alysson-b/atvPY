# Vamos começar pedindo as entradas do usuário

# Pedindo o capital inicial, ou seja, quanto a pessoa quer investir.
capital_inicial = float(input("Digite o capital inicial (em reais): "))

# Pedindo a taxa de juros. Aqui esperamos que o usuário digite a taxa como um percentual,
# então precisamos dividir por 100 para transformar em decimal.
taxa_juros = float(input("Digite a taxa de juros anual (em %): ")) / 100

# Pedindo o tempo de aplicação, ou seja, por quantos anos o dinheiro vai ficar rendendo.
tempo = float(input("Digite o tempo de aplicação (em anos): "))

# Aplicando a fórmula de juros simples. Aqui calculamos o valor futuro do investimento.
valor_futuro = capital_inicial * (1 + taxa_juros * tempo)

# Exibindo o resultado para o usuário. Estamos usando uma f-string, que é uma maneira fácil
# de incluir variáveis em uma string (texto) em Python. O {valor_futuro:.2f} significa que
# queremos exibir o valor com 2 casas decimais.
print(f"O valor futuro do investimento será de R$ {valor_futuro:.2f}")
