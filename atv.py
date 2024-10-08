# Perguntamos ao usuário quanto ele ganha por hora.
# Usamos a função input() para pegar a informação digitada.
# Precisamos converter a resposta para float (número decimal), pois input() sempre retorna uma string (texto).

salario_por_hora = float(input("Quanto você ganha por hora? "))

# Agora, perguntamos ao usuário quantas horas ele trabalhou no mês.
# Novamente, usamos a função input() e convertemos para float.

horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

# Agora fazemos o cálculo. Multiplicamos o valor por hora pelo número de horas.
# O resultado será armazenado na variável salario_total.

salario_total = salario_por_hora * horas_trabalhadas

# Finalmente, usamos a função print() para exibir o resultado.
# Aqui, usamos uma f-string, que é uma forma fácil e eficiente de incluir variáveis dentro de um texto.
# O "f" antes das aspas permite que coloquemos o valor da variável dentro de chaves {}.

print(f"Seu salário total no mês é: R$ {salario_total:.2f}")
