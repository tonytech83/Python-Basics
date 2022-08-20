loads_number = int(input())

bus_weight = 0
truck_weight = 0
train_weight = 0
overall_weight = 0
price = 0

for load in range(loads_number):
    load_weight = int(input())
    overall_weight += load_weight

    if load_weight <= 3:
        bus_weight += load_weight
        price += load_weight * 200
    elif 4 <= load_weight <= 11:
        truck_weight += load_weight
        price += load_weight * 175
    elif load_weight >= 12:
        train_weight += load_weight
        price += load_weight * 120

average_price = price / overall_weight
average_bus = bus_weight / overall_weight * 100
average_truck = truck_weight / overall_weight * 100
average_train = train_weight / overall_weight * 100

print(f'{average_price:.2f}')
print(f'{average_bus:.2f}%')
print(f'{average_truck:.2f}%')
print(f'{average_train:.2f}%')
