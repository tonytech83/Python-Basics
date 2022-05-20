annual_tax = int(input())

sneakers = annual_tax - (annual_tax * 0.4)
equipment = sneakers - (sneakers * 0.2)
ball = equipment / 4
accessories = ball / 5

total_spend = annual_tax + sneakers + equipment + ball + accessories

print(total_spend)
