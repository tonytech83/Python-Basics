def sum_seconds(f_time, s_time, t_time):
    result = f_time + s_time + t_time
    minutes = result // 60
    second = result % 60
    if second < 10:
        print(f"{minutes}:0{second}")
    else:
        print(f"{minutes}:{second}")


first_time = int(input())
second_time = int(input())
third_time = int(input())

sum_seconds(first_time, second_time, third_time)
