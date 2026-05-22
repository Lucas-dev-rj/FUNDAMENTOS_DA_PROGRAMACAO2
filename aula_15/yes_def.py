#Desenvolva um sistema de pizzaria onde será recebido o preço do pedido, um desconto de 10%, e ao final exiba o valor total do pedido com esse desconto;

#declarar uma def (função)
def calcular_total(nome, preco, desconto=0.10):
    valor_desconto = preco * desconto
    total = preco - valor_desconto
    print(f""" RECIBO
          Pedido do cliente: {nome}
          Valor do peido: R$ {preco}
          desconto aplicado: {desconto}
          total do pedido: R$ {total:.2f}
        """)

#Invocação da def 
calcular_total("joão",45.90)
calcular_total("Ana",38.50)
calcular_total("Maria",20)
calcular_total("Rian",19)
calcular_total("Kitty",9.99)
