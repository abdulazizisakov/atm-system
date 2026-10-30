# 🏦 ATM System — Bankomat boshqaruv tizimi

## 📌 Project haqida

**ATM System** — Python dasturlash tilida OOP (Object-Oriented Programming) tamoyillari asosida ishlab chiqiladigan bankomat boshqaruv tizimi.

Dastur foydalanuvchilarga bank hisobini yaratish, karta raqami va PIN-kod orqali tizimga kirish, balansni tekshirish, hisobga pul kiritish, pul yechish va amalga oshirilgan tranzaksiyalar tarixini ko‘rish imkoniyatlarini taqdim etadi.

Loyiha real bankomat faoliyatini soddalashtirilgan shaklda modellashtiradi.

## 🎯 Project maqsadi

Python dasturlash tilidagi OOP bilimlarini amaliyotda qo‘llash va mustahkamlash.

Loyiha davomida o‘quvchilar:
- Class va Object yaratish.
- Constructor (`__init__`) bilan ishlash.
- Attributes va Methods yaratish.
- Encapsulation tamoyilini qo‘llash.
- Bir nechta class o‘rtasida bog‘lanish tashkil qilish.
- Obyektlar orqali ma'lumotlarni boshqarish.
- Real hayotdagi biznes jarayonlarini modellashtirishni o‘rganadilar.

## ⚙️ Asosiy imkoniyatlari

### 1. Account Management
- Yangi bank hisobini yaratish.
- Hisob egasining ma'lumotlarini saqlash.
- Unikal karta raqami yaratish.
- PIN-kod o‘rnatish.

### 2. Authentication
- Karta raqami orqali hisobni aniqlash.
- PIN-kod orqali tizimga kirish.
- Noto‘g‘ri PIN-kod kiritilganda xatolik chiqarish.
- Noto‘g‘ri urinishlar sonini cheklash.

### 3. Banking Operations
- Balansni tekshirish (Balance).
- Hisobga pul kiritish (Deposit).
- Hisobdan pul yechish (Withdraw).
- Hisobdagi mablag‘ yetarliligini tekshirish.

### 4. Transaction History
- Barcha tranzaksiyalarni saqlash.
- Pul kiritish operatsiyalarini ko‘rsatish.
- Pul yechish operatsiyalarini ko‘rsatish.
- Tranzaksiya sanasi va summasini ko‘rsatish.

### 5. Security
- PIN-kodni tekshirish.
- Noto‘g‘ri urinishlarni nazorat qilish.
- Mablag‘ yetarli bo‘lmaganda pul yechishga ruxsat bermaslik.
- Tizimdan xavfsiz chiqish.

## 🧩 Loyihada ishlatiladigan texnologiyalar

- Python 3
- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructor (`__init__`)
- Instance Attributes
- Instance Methods
- Encapsulation
- Lists and Dictionaries
- Conditional Statements
- Loops
- Exception Handling
- Random Module
- Datetime Module

## 📁 Project Structure

    ATM_Project/
    │
    ├── main.py
    ├── account.py
    ├── atm.py
    ├── transaction.py
    │
    └── README.md

### Fayllarning vazifalari

| File | Vazifasi |
|---|---|
| main.py | Dasturni ishga tushirish va asosiy menu |
| account.py | Bank hisobini boshqarish |
| atm.py | Bankomat faoliyatini boshqarish |
| transaction.py | Tranzaksiyalarni boshqarish |
| README.md | Loyiha haqida hujjatlashtirish |

## 🏗️ Classlar, Attributes va Methods

### 1. Account Class

**Vazifasi:** Foydalanuvchining bank hisob ma'lumotlarini saqlash va boshqarish.

**Attributes:**

| Attribute | Type | Description |
|---|---|---|
| id | int | Hisob ID raqami |
| egasi | str | Hisob egasining ismi |
| karta_raqami | str | Bank kartasi raqami |
| pin | str | Karta PIN-kodi |
| balans | float | Hisobdagi mablag‘ |
| tranzaksiyalar | list | Hisob tranzaksiyalari |

**Methods:**
- `balansni_korish()` — hisobdagi mablag‘ni ko‘rsatish.
- `pul_qoshish()` — hisobga pul kiritish.
- `pul_yechish()` — hisobdan pul yechish.
- `pin_tekshirish()` — PIN-kodni tekshirish.

### 2. ATM Class

**Vazifasi:** Bankomatning asosiy faoliyatini boshqarish.

**Attributes:**

| Attribute | Type | Description |
|---|---|---|
| nomi | str | Bankomat nomi |
| hisoblar | list | Tizimdagi bank hisoblari |
| joriy_hisob | Account | Hozir tizimga kirgan foydalanuvchi hisobi |
| urinishlar | int | PIN-kod kiritish urinishlari |

**Methods:**
- `hisob_yaratish()` — yangi bank hisobini yaratish.
- `tizimga_kirish()` — karta va PIN-kod orqali autentifikatsiya qilish.
- `hisobni_topish()` — karta raqami orqali hisobni topish.
- `menu()` — bankomat menyusini chiqarish.
- `tizimdan_chiqish()` — foydalanuvchi sessiyasini yakunlash.

### 3. Transaction Class

**Vazifasi:** Bank hisobida amalga oshirilgan operatsiyalarni boshqarish va tarixini saqlash.

**Attributes:**

| Attribute | Type | Description |
|---|---|---|
| id | int | Tranzaksiya ID raqami |
| turi | str | Deposit yoki Withdraw |
| summa | float | Tranzaksiya summasi |
| sana | datetime | Tranzaksiya amalga oshirilgan vaqt |

**Methods:**
- `malumot()` — tranzaksiya haqida ma'lumot chiqarish.
- `tranzaksiya_tarixi()` — tranzaksiyalar tarixini ko‘rsatish.

## 📋 Main Menu

Dastur ishga tushganda quyidagi menyu chiqishi kerak:

### ATM System

1. Yangi hisob yaratish
2. Tizimga kirish
3. Dasturni yakunlash

### User Menu

1. Balansni tekshirish
2. Pul kiritish (Deposit)
3. Pul yechish (Withdraw)
4. Tranzaksiyalar tarixini ko‘rish
5. PIN-kodni o‘zgartirish
6. Tizimdan chiqish

## 📏 Business Rules

1. Har bir bank hisobining unikal ID raqami bo‘lishi kerak.
2. Har bir bank kartasining unikal karta raqami bo‘lishi kerak.
3. PIN-kod 4 xonali bo‘lishi kerak.
4. Foydalanuvchi faqat to‘g‘ri karta raqami va PIN-kod orqali tizimga kira olishi kerak.
5. Noto‘g‘ri PIN-kod 3 marta kiritilsa, karta vaqtincha bloklanishi kerak.
6. Pul kiritish summasi musbat bo‘lishi kerak.
7. Pul yechish summasi balansdan oshmasligi kerak.
8. Har bir Deposit va Withdraw operatsiyasi tranzaksiyalar tarixiga yozilishi kerak.
9. Tranzaksiya uchun unikal ID va amalga oshirilgan vaqt saqlanishi kerak.
10. Tizimdan chiqilganda joriy foydalanuvchi sessiyasi yakunlanishi kerak.

## ▶️ Dasturni ishga tushirish

Terminal orqali loyiha papkasiga o'ting va quyidagi buyruqni bajaring:

    python main.py

## 📊 Project darajasi

**Intermediate (O‘rta daraja)**

## 📚 O‘rganiladigan bilimlar

Ushbu loyiha orqali o‘quvchilar:

- Python OOP asoslarini.
- Class va Object tushunchalarini.
- Constructor va Instance Attributes bilan ishlashni.
- Encapsulation tamoyilini.
- Classlar o‘rtasidagi munosabatlarni.
- Object Composition asoslarini.
- Methods orqali biznes logikani tashkil qilishni.
- Lists orqali obyektlar kolleksiyasini boshqarishni.
- Exception Handling yordamida xatolarni boshqarishni o‘rganadilar.

---

**Project type:** Educational / Practice Project

**Language:** Python 3

**Architecture:** Modular OOP

**Difficulty:** Intermediate
