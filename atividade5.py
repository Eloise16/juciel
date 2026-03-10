valor= float(input("digite o valor da compra: "))

if valor > 100:
     desconto = valor * 0.10
     valor_final = valor - desconto 
     print("valor com 10% de desconto:", valor_final)
else:
     print("valor da compra:", valor)