budget = float(input())
vga_count = int(input())
cpu_count = int(input())
ram_count = int(input())

vga_total_price = vga_count * 250
cpu_total_price = cpu_count * vga_total_price * 0.35
ram_total_price = ram_count * vga_total_price * 0.1

total_price = vga_total_price + cpu_total_price + ram_total_price

if vga_count > cpu_count:
    total_price = total_price * 0.85

diff = abs(budget - total_price)

if total_price <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
