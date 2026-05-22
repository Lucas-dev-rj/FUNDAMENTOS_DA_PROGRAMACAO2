# Variaveis da pizzaria
FRETE = 2 #Constante fake
pizza_sabor= input("informe o sabor da pizza - [frango com requeijao], [calabresa], [mussarela], [banana com chocolate]: ")
pizza_tamanho= input("informe o tamanho da pizza - [pequena], [média], [grande]: ")
dia_semana= input("informe o dia da semana - [quarta], [quinta], [sexta], [sabado], [domingo]: ")

print(f" o sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}.")
#promoções -> Estruturas condicionais

# comprando qualquer pizza e qualquer tamanho no sabado, 
# o refri é gratuito.
if dia_semana == "sabado":
    print(f"🍕pedido aceito com sucesso")
    print(f"o refri hoje é por conta da casa")
elif dia_semana == "domingo":  
    print(f"🍕pedido aceito com sucesso")
    print(f"o frete e o refri hoje é por conta da casa")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print(f"🍕pedido aceito com sucesso")
    print(f"o frete hoje é por conta da casa")


# comprando uma pizza calabresa tamanho médio, o frete é gratuito. 

#comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri sao gratuitos.