city = input()
quantity_of_sells = float(input())

commission = 0

if city == "Sofia":
    if 0 <= quantity_of_sells <= 500:
        commission = 0.05
    elif 500 < quantity_of_sells <= 1000:
        commission = 0.07
    elif 1000 < quantity_of_sells <= 10000:
        commission = 0.08
    else:
        commission = 0.12

if city == "Varna":
    if 0 <= quantity_of_sells <= 500:
        commission = 0.045
    elif 500 < quantity_of_sells <= 1000:
        commission = 0.075
    elif 1000 < quantity_of_sells <= 10000:
        commission = 0.1
    else:
        commission = 0.13

if city == "Plovdiv":
    if 0 <= quantity_of_sells <= 500:
        commission = 0.055
    elif 500 < quantity_of_sells <= 1000:
        commission = 0.08
    elif 1000 < quantity_of_sells <= 10000:
        commission = 0.12
    else:
        commission = 0.145

if commission == 0 or quantity_of_sells < 0:
    print("error")
else:
    print(f"{(quantity_of_sells * commission):.2f}")
