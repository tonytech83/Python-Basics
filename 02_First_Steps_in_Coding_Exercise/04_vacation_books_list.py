total_count_pages = int(input())
pages_per_hour = int(input())
days_for_read = int(input())

total_read_hours = total_count_pages // pages_per_hour
hours_per_day = total_read_hours // days_for_read

print(hours_per_day)
