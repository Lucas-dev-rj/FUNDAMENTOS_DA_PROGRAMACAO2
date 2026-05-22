# Estrutura de repetição
# if (se) -> Verifica se uma condição é true(verdadeira).Se for, ele executa o código.
# elif (senão se) -> é usado para testar várias condições. Ele só executa se todas as condições anteriores forem falsas.
# else (senão) -> Executa o código se a condição if for false(falsa).
# idade_usuario = 15
# # se o usuário for maior de 18 anos, eu vou passar a informação:Você é maior de idade, senão Você é menor de idade.
# if idade_usuario >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade")
idade = 73
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 0 and idade < 18:
    print("Você é jovem de idade.")
elif idade >= 70:
    print("Você é experiente de idade.")
else:
    print("Você é menor de idade.")  