sal = float(input("Digite o valor do salário em R$: "))
if sal > 1250:
    aum = sal + (sal * 10 / 100)
    print("O salário tem um aumento de 10%, ficando R${:.2f}".format(aum))
else:
    aum = sal + (sal * 15 / 100)
    print("O salário tem um aumento de 15%, fica ndo R${:.2f}".format(aum))