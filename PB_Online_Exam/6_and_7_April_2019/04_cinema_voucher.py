voucher = int(input())

purchase = input()

sum_of_purchases = 0
tickets = 0
other = 0

while purchase != "End":

    if len(purchase) > 8:
        first_chr = purchase[0]
        second_chr = purchase[1]
        first_chr_to_decimal = ord(first_chr)
        second_chr_to_decimal = ord(second_chr)
        sum_of_purchases += (first_chr_to_decimal + second_chr_to_decimal)
        if voucher - sum_of_purchases < 0:
            break
        tickets += 1

    else:
        first_chr = purchase[0]
        first_chr_to_decimal = ord(first_chr)
        sum_of_purchases += first_chr_to_decimal
        if voucher - sum_of_purchases < 0:
            break
        other += 1

    purchase = input()

print(f"{tickets}")
print(f"{other}")
