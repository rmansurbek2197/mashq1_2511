hujjat = input("Hujjat topshirilganmi? (ha/yo'q): ").lower()
intervyu = input("Suhbatdan o'tdingizmi? (ha/yo'q): ").lower()
test = input("Test sinovidan o'tdingizmi? (ha/yo'q): ").lower()


if hujjat == "ha" and intervyu == "ha" and test == "ha":
    print("Siz ishga qabul qilindingiz!")

elif hujjat == "yo'q":
    print("Avvalo hujjatlaringizni topshiring.")

elif hujjat == "ha" and intervyu == "yo'q":
    print("Suhbatdan o'tmagansiz.")

elif hujjat == "ha" and intervyu == "ha" and test == "yo'q":
    print("Test natijalari yetarli emas.")

else:
    print("Jarayon davom etmoqda.")
