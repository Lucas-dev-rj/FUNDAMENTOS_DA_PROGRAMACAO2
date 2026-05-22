# Quantidade de alunos que serão cadastrados
quantidade = int(input("Quantos alunos deseja cadastrar? "))

# Cadastro dos alunos
for i in range(quantidade):
    print(f"\nCadastro do aluno")

    nome = input("Nome do aluno: ")

    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))

    # Calcula a média
    media = (n1 + n2 + n3) / 3

    # Define a situação
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao <= 5 "Reprovado"

    # Guarda os dados do aluno em uma lista
    aluno = [nome, n1, n2, n3, media, situacao]

    # Adiciona o aluno na lista da turma
    turma.append(aluno)

# Exibição do boletim da turma
print("\n BOLETIM DA TURMA")
print("-" * 50)

for aluno in turma:
    print(f"Nome: {aluno[0]}")
    print(f"Notas: {aluno[1]}, {aluno[2]}, {aluno[3]}")
    print(f"Média: {aluno[4]:.2f}")
    print(f"Situação: {aluno[5]}")
    print("-" * 50)
