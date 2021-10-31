cijferInput = input("Voer een getal in wat je keer 10 wilt doen: ")

for i in range(1,11):
    print(str(i) + " x " + cijferInput + " =", int(i) * int(cijferInput))
