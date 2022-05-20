def pass_correct(psw):
    if psw == "s3cr3t!P@ssw0rd":
        return "Welcome"
    else:
        return "Wrong password!"


password = input()

print(pass_correct(password))
