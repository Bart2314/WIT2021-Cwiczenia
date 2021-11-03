username = "admin"
password = 1234

username1 = input(("Podaj login: "))
password1 = input(("Podaj hasło: "))

while username1 != username and password1 != password:
    print("Login lub/i hasło są niepoprawne")
    username1 = input(("Podaj login: "))
    password1 = input(("Podaj hasło: "))

print("OK")




