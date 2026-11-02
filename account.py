from transaction import Transaction


class Account:
    def __init__(self, id, egasi, karta_raqami, pin):
        self.__tekshir_pin(pin)
        self.__id = id
        self.__egasi = egasi
        self.__karta_raqami = karta_raqami
        self.__pin = pin
        self.__balans = 0.0
        self.__tranzaksiyalar = []

    @staticmethod
    def __tekshir_pin(pin):
        if not (isinstance(pin, str) and pin.isdigit() and len(pin) == 4):
            raise ValueError("PIN-kod 4 xonali raqam bo'lishi kerak.")

    @property
    def id(self):
        return self.__id

    @property
    def egasi(self):
        return self.__egasi

    @property
    def karta_raqami(self):
        return self.__karta_raqami

    @property
    def balans(self):
        return self.__balans

    @property
    def tranzaksiyalar(self):
        return list(self.__tranzaksiyalar)

    def balansni_korish(self):
        print(f"Balans: {self.__balans:,.2f} so'm")

    def pul_qoshish(self, summa):
        if summa <= 0:
            raise ValueError("Pul kiritish summasi musbat bo'lishi kerak.")
        self.__balans += summa
        self.__tranzaksiyalar.append(Transaction("Deposit", summa))

    def pul_yechish(self, summa):
        if summa <= 0:
            raise ValueError("Pul yechish summasi musbat bo'lishi kerak.")
        if summa > self.__balans:
            raise ValueError("Hisobda mablag' yetarli emas.")
        self.__balans -= summa
        self.__tranzaksiyalar.append(Transaction("Withdraw", summa))

    def pin_tekshirish(self, pin):
        return self.__pin == pin

    def pin_ozgartirish(self, eski_pin, yangi_pin):
        if not self.pin_tekshirish(eski_pin):
            raise ValueError("Eski PIN-kod noto'g'ri.")
        self.__tekshir_pin(yangi_pin)
        self.__pin = yangi_pin