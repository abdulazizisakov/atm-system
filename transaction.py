from datetime import datetime


class Transaction:
    _keyingi_id = 1

    def __init__(self, turi, summa):
        if turi not in ("Deposit", "Withdraw"):
            raise ValueError("Tranzaksiya turi Deposit yoki Withdraw bo'lishi kerak.")
        self.__id = Transaction._keyingi_id
        Transaction._keyingi_id += 1
        self.__turi = turi
        self.__summa = summa
        self.__sana = datetime.now()

    @property
    def id(self):
        return self.__id

    @property
    def turi(self):
        return self.__turi

    @property
    def summa(self):
        return self.__summa

    @property
    def sana(self):
        return self.__sana

    def malumot(self):
        print(f"#{self.id} | {self.turi} | {self.summa:,.2f} so'm | "
              f"{self.sana.strftime('%Y-%m-%d %H:%M:%S')}")

    @staticmethod
    def tranzaksiya_tarixi(tranzaksiyalar):
        if not tranzaksiyalar:
            print("Tranzaksiyalar mavjud emas.")
            return
        for t in tranzaksiyalar:
            t.malumot()