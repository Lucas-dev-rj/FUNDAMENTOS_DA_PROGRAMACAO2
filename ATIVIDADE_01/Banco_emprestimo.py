print("Sistema de emprestimo bancario")

#Entrada de dados
idade = int(input("digite a idade"))
salario = float(input("digite o salario do cliente"))
tempo_trabalho = int(input("digite o tempo de trabalho em anos"))

# Estruturas condicionais
if idade < 18:
    print("emprestimo negado. Cliente menor de idade")
elif salario >= 5000: 
    print("Emprestimo aprovado automaticamente.")
elif idade >=18 and salario >=2000 and tempo_trabalho >=2:
    print("emprestimo aprovado.")

else: 
    print("emprestimo negado")

