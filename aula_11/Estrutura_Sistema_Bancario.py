#Solicitar dados do cliente
idade_cliente= input("digite a sua idade: ")
salario_cliente= int (input("digite o seu salario (R$): "))
tempo_trabalho_cliente= int (input("digite o tempo de carteira assinada em anos: "))


#verificar aprovação 
if idade_cliente < 18:
    print(f"emprestimo negado")

elif salario_cliente >= 5000:
    print(f"Aprovacao automatica")

elif idade_cliente >= 18 and salario_cliente >= 2000 and tempo_trabalho_cliente >= 2:
    print(f"emprestimo aprovado")


else:
   print("emprestimo negado")

