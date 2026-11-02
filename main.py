from atm import ATM
from transaction import Transaction


def summa_kiritish(matn):
    while True:
        try:
            return float(input(matn).strip())
        except ValueError:
            print("Xato: iltimos, son kiriting.")


def hisob_yaratish(atm):
    egasi = input("Ism: ")
    pin = input("PIN-kod (4 xonali): ")
    hisob = atm.hisob_yaratish(egasi, pin)
    print("Hisob yaratildi!")
    print(f"Karta raqami: {hisob.karta_raqami}")


def tizimga_kirish(atm):
    karta = input("Karta raqami: ").strip()
    while True:
        pin = input("PIN-kod: ").strip()
        try:
            atm.tizimga_kirish(karta, pin)
            return True
        except ValueError as xato:
            print(f"Xatolik: {xato}")
            if atm.hisobni_topish(karta) is None or atm.bloklangan_mi(karta):
                return False


def foydalanuvchi_menu(atm):
    hisob = atm.joriy_hisob
    print(f"\nXush kelibsiz, {hisob.egasi}!")
    while True:
        print("\n--- User Menu ---")
        print("1. Balansni tekshirish")
        print("2. Pul kiritish (Deposit)")
        print("3. Pul yechish (Withdraw)")
        print("4. Tranzaksiyalar tarixini ko'rish")
        print("5. PIN-kodni o'zgartirish")
        print("6. Tizimdan chiqish")
        tanlov = input("Tanlang: ").strip()
        try:
            if tanlov == "1":
                hisob.balansni_korish()
            elif tanlov == "2":
                hisob.pul_qoshish(summa_kiritish("Summa: "))
                print("Pul hisobga kiritildi.")
            elif tanlov == "3":
                hisob.pul_yechish(summa_kiritish("Summa: "))
                print("Pul yechildi.")
            elif tanlov == "4":
                Transaction.tranzaksiya_tarixi(hisob.tranzaksiyalar)
            elif tanlov == "5":
                eski = input("Eski PIN-kod: ").strip()
                yangi = input("Yangi PIN-kod (4 xonali): ").strip()
                hisob.pin_ozgartirish(eski, yangi)
                print("PIN-kod o'zgartirildi.")
            elif tanlov == "6":
                atm.tizimdan_chiqish()
                print("Tizimdan chiqdingiz.")
                break
            else:
                print("Xato: menyuda bunday band yo'q.")
        except ValueError as xato:
            print(f"Xatolik: {xato}")


def main():
    atm = ATM("ATM System")
    while True:
        atm.menu()
        tanlov = input("Tanlang: ").strip()
        try:
            if tanlov == "1":
                hisob_yaratish(atm)
            elif tanlov == "2":
                if tizimga_kirish(atm):
                    foydalanuvchi_menu(atm)
            elif tanlov == "3":
                print("Xayr!")
                break
            else:
                print("Xato: menyuda bunday band yo'q.")
        except ValueError as xato:
            print(f"Xatolik: {xato}")


if __name__ == "__main__":
    main()