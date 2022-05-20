wr = float(input())
distance = float(input())
dist_per_sec = float(input())

record_without_resistance = distance * dist_per_sec

# seconds delay of resistance
delay_of_resistance = distance // 15 * 12.5

personal_record_after_resistance = record_without_resistance + delay_of_resistance

diff = abs(wr - personal_record_after_resistance)

if personal_record_after_resistance < wr:
    print(f"Yes, he succeeded! The new world record is {personal_record_after_resistance:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")

