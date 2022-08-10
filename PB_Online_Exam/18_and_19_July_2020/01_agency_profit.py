company_name = input()
adult_tickets = int(input())
kid_tickets = int(input())
adult_tk_price = float(input())
tax_price = float(input())

total_adults = adult_tickets * (adult_tk_price + tax_price)
kid_tk_price = adult_tk_price * 0.3
total_kids = kid_tickets * (kid_tk_price + tax_price)

total = total_adults + total_kids

profit = total * 0.2

print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')
