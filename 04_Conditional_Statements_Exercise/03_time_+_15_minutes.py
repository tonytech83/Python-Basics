def time_plus_15(h, m):
    m += 15
    if m > 59:
        h += 1
        m = m - 60

    if h > 23:
        h = h - 24

    if m >= 10:
        print(f"{h}:{m}")
    else:
        print(f"{h}:0{m}")


hours = int(input())
minutes = int(input())

time_plus_15(hours, minutes)
