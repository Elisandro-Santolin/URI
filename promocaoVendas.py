## 9 - Uma determinada loja está fazendo promoções de vendas. Qualquer compra que um cliente fizer até R$ 100,00 receberá 5% de descontos. Se a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de 20%. ##

print("## Promoção de Vendas ###")

valorCompra = float(input("Digite o valor total da compra: "))

if(valorCompra <= 100):
    valorDesconto = ((valorCompra * 5)/ 100) 
    valorFinal = (valorCompra - valorDesconto)
    print(f'Valor final com desconto: {valorFinal:.2f}')
elif(valorCompra > 100 and valorCompra <= 200):
    valorDesconto = ((valorCompra * 10) / 100)
    valorFinal = (valorCompra - valorDesconto)
    print(f'Valor final com desconto: {valorFinal:.2f}')
else:
    valorDesconto = ((valorCompra * 20) / 100)
    valorFinal = (valorCompra - valorDesconto)
    print(f'Valor final com desconto: {valorFinal:.2f}')