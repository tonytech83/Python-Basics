username = input()
password = input()

while True:
    current_password = input()
    if current_password == password:
        break

print(f"Welcome {username}!")
