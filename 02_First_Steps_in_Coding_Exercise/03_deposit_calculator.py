deposit_amount = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input())

per_year = deposit_amount * (annual_interest_rate / 100)
per_month = per_year / 12

total = deposit_amount + (per_month * term_of_deposit)

print(f"{total:.2f}")
