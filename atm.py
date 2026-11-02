import random
from account import Account

MAX_URINISH = 3


class ATM:
    def __init__(self, nomi):
        self.__nomi = nomi
        self.__hisoblar = []
        self.__joriy_hisob = None
        self.__urinishlar = 0
        self.__bloklangan = set()
        self.__oxirgi_karta = None

    @property
    def nomi(self):
        return self.__nomi

    @property
    def joriy_hisob(self):
        return self.__joriy_hisob

    @property
    def urinishlar(self):
        return self.__urinishlar

    def __karta_yaratish(self):
        while True:
            karta = str(random.randint(10**15, 10**16 - 1))
            if self.hisobni_topish(karta) is None:
                return karta

    def hisob_yaratish(self, egasi, pin):
        if not egasi.strip():
            raise ValueError("Hisob egasining ismi bo'sh bo'lmasligi kerak.")
        hisob = Account(len(self.__hisoblar) + 1, egasi.strip(),
                        self.__karta_yaratish(), pin)
        self.__hisoblar.append(hisob)
        return hisob

    def hisobni_topish(self, karta_raqami):
        for hisob in self.__hisoblar:
            if hisob.karta_raqami == karta_raqami:
                return hisob
        return None

    def bloklangan_mi(self, karta_raqami):
        return karta_raqami in self.__bloklangan

    def tizimga_kirish(self, karta_raqami, pin):
        hisob = self.hisobni_topish(karta_raqami)
        if hisob is None:
            raise ValueError("Bunday karta raqami topilmadi.")
        if self.bloklangan_mi(karta_raqami):
            raise ValueError("Karta vaqtincha bloklangan.")
        if karta_raqami != self.__oxirgi_karta:
            self.__urinishlar = 0
            self.__oxirgi_karta = karta_raqami
        if hisob.pin_tekshirish(pin):
            self.__urinishlar = 0
            self.__joriy_hisob = hisob
            return hisob
        self.__urinishlar += 1
        if self.__urinishlar >= MAX_URINISH:
            self.__bloklangan.add(karta_raqami)
            raise ValueError("PIN-kod 3 marta noto'g'ri kiritildi. "
                             "Karta vaqtincha bloklandi.")
        raise ValueError("PIN-kod noto'g'ri. Qolgan urinishlar: "
                         f"{MAX_URINISH - self.__urinishlar}")

    def menu(self):
        print(f"\n=== {self.__nomi} ===")
        print("1. Yangi hisob yaratish")
        print("2. Tizimga kirish")
        print("3. Dasturni yakunlash")

    def tizimdan_chiqish(self):
        self.__joriy_hisob = None