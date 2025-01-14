
# # # # # # # # # # # # xona_boyi = float(input("Xona bo'yi (metr): "))
# # # # # # # # # # # # xona_eni = float(input("Xona eni (metr): "))
# # # # # # # # # # # # xona_balandligi = float(input("Xona balandligini kiriting (metr): "))

# # # # # # # # # # # # xona_devori = xona_boyi * xona_balandligi
# # # # # # # # # # # # xona_devori2 = xona_eni * xona_balandligi

# # # # # # # # # # # # hajmi = 0.7 * (xona_boyi_kv * xona_eni_kv)


# # # # # # # # # # # # print(f"Xona bo'yi: {xona_boyi} metr")
# # # # # # # # # # # # print(f"Xona eni: {xona_eni} metr")
# # # # # # # # # # # # print(f"Xona bo'yoq hajmi: {hajmi} kg")

# # # # # # # # # # # # age = int(input("your age: "))
# # # # # # # # # # # # money = int(input("How much you have"))
# # # # # # # # # # # # if ( age > 21 ):
# # # # # # # # # # # #     print("Assalomu Alekum")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("GO to home bitch")

# # # # # # # # # # # # if (money > 1000):
# # # # # # # # # # # #     print("Xush kelibsiz")
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("Mablag yetarlik emas")



# # # # # # # # # # # # if ( 001, 002, 003,):
# # # # # # # # # # # #     print("bepul")
# # # # # # # # # # # # class Parkovka:
# # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # #         self.admin_kirganmi = False
# # # # # # # # # # # #         self.ishchi_kirganmi = False
# # # # # # # # # # # #         self.avtomobillar = []

# # # # # # # # # # # #     def admin_kirish(self):
# # # # # # # # # # # #         if not self.admin_kirganmi:
# # # # # # # # # # # #             print("Admin kirildi!")
# # # # # # # # # # # #             self.admin_kirganmi = True
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             print("Admin allaqachon kirgan")

# # # # # # # # # # # #     def ishchi_kirish(self):
# # # # # # # # # # # #         if not self.ishchi_kirganmi:
# # # # # # # # # # # #             print("Ishchi kirildi!")
# # # # # # # # # # # #             self.ishchi_kirganmi = True
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             print("Ishchi allaqachon kirgan")

# # # # # # # # # # # #     def avtomobil_kirish(self, nomi):
# # # # # # # # # # # #         if self.ishchi_kirganmi:
# # # # # # # # # # # #             self.avtomobillar.append(nomi)
# # # # # # # # # # # #             print(f"{nomi} avtomobili kirildi!")
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             print("Ishchi kirilmaganligi sababli avtomobil kirila olmaydi!")

# # # # # # # # # # # #     def avtomobil_chiqarish(self, nomi):
# # # # # # # # # # # #         if self.ishchi_kirganmi:
# # # # # # # # # # # #             if nomi in self.avtomobillar:
# # # # # # # # # # # #                 self.avtomobillar.remove(nomi)
# # # # # # # # # # # #                 print(f"{nomi} avtomobili chiqarildi!")
# # # # # # # # # # # #             else:
# # # # # # # # # # # #                 print(f"{nomi} avtomobili topilmadi!")
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             print("Ishchi kirilmaganligi sababli avtomobil chiqarila olmaydi!")

# # # # # # # # # # # # # Dasturni ishlatish
# # # # # # # # # # # # parkovka = Parkovka()
# # # # # # # # # # # # parkovka.admin_kirish()
# # # # # # # # # # # # parkovka.ishchi_kirish()
# # # # # # # # # # # # parkovka.avtomobil_kirish("Toyota")
# # # # # # # # # # # # parkovka.avtomobil_chiqarish("BMW")

# # # # # # # # # # # # admin = ["001","002","003"]
# # # # # # # # # # # # ischi = ["004","005","006"]

# # # # # # # # # # # # berilgan_raqam = input()

# # # # # # # # # # # # if berilgan_raqam in admin:
# # # # # # # # # # # #     print("tekin")
# # # # # # # # # # # # elif berilgan_raqam in admin:
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("pullik")	   
# # # # # # # # # # # # admin = ['001', '002', '003']
# # # # # # # # # # # # ishchi = ['004', '005', '006']
# # # # # # # # # # # # J = (input("Moshina nomeri: "))
# # # # # # # # # # # # if J in ishchi:
# # # # # # # # # # # #     print("Pul to'la")
# # # # # # # # # # # #     if J in admin:
# # # # # # # # # # # #         print("Xush Kelibsiz")
# # # # # # # # # # # # else: 
# # # # # # # # # # # #     print("Sizga Parkovka taqiqlanadi") 

# # # # # # # # # # # #     Menga rasmga olinmaydi
# # # # # # # # # # # # int(input("mashina raqamini kiriting: "))
# # # # # # # # # # # # if input not in ["vsf", "uzb", "ppp"]:
# # # # # # # # # # # #     print("shtraf") 
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print("okay")
# # # # # # # # # # # # mytuples = (21, "oasis", 35.7)
# # # # # # # # # # # # print(mytuples [0])
# # # # # # # # # # # # mevalar = {
# # # # # # # # # # # #     'olma': 1500,
# # # # # # # # # # # #     'shaftoli': 3000,
# # # # # # # # # # # #     'uzum': 2500,
# # # # # # # # # # # #     'banan': 2000,
# # # # # # # # # # # #     'nok': 1800,
# # # # # # # # # # # #     'gilos': 2000,
# # # # # # # # # # # #     'olcha': 5000,
# # # # # # # # # # # #     'dragon': 10000,
# # # # # # # # # # # #     'anjir': 4000
# # # # # # # # # # # # }

# # # # # # # # # # # # def pul_hisobla(turi, kilogram):
# # # # # # # # # # # #     if turi in mevalar:
# # # # # # # # # # # #         narx = mevalar[turi]
# # # # # # # # # # # #         miqdor_pul = narx * kilogram
# # # # # # # # # # # #         return miqdor_pul
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         return "Kechirasiz, bunday meva yo'q."

# # # # # # # # # # # # def main():
# # # # # # # # # # # #     print("Meva turini tanlang:")
# # # # # # # # # # # #     for meva in mevalar:
# # # # # # # # # # # #         print(meva)

# # # # # # # # # # # #     meva_turi = input("Meva turi kiriting: ").lower()

# # # # # # # # # # # #     if meva_turi in mevalar:
# # # # # # # # # # # #         kilogram = float(input(f"{meva_turi.capitalize()} necha kilogram olishni xohlaysiz? "))
# # # # # # # # # # # #         miqdor_pul = pul_hisobla(meva_turi, kilogram)
# # # # # # # # # # # #         print(f"{kilogram} kilogram {meva_turi} narxi: {miqdor_pul} so'm")
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         print("Kechirasiz, bunday meva yo'q.")

# # # # # # # # # # # # if name == "main":
# # # # # # # # # # # #     main()



# # # # # # # # # # # # count = 0
# # # # # # # # # # # # while (count < 3):
# # # # # # # # # # # #     count = count + 1	
# # # # # # # # # # # #     print("hello world")	
# # # # # # # # # # # # # maxsulotlar = {
# # # # # # # # # # # # #     "olma" : 1000,
# # # # # # # # # # # # #     "uzum" : 2000,
# # # # # # # # # # # # #     "nok" : 3000,
# # # # # # # # # # # # #     "gilos" : 4000,
# # # # # # # # # # # # #     "olcha" : 5000,
# # # # # # # # # # # # #     "dragon" : 6000,
# # # # # # # # # # # # #     "anjir" : 7000
# # # # # # # # # # # # # }
# # # # # # # # # # # # # print("Xush kelibsiz")
# # # # # # # # # # # # # print(maxsulotlar)
# # # # # # # # # # # # # maxsulot = input("Maxsulotni nomini kiriting")
# # # # # # # # # # # # # umumiy_summ = 0
# # # # # # # # # # # # # while(maxsulot != "toxta"):
# # # # # # # # # # # # #     maxsulot_xajmi = float(input("Qancha xoxlaysiz:   "))
# # # # # # # # # # # # #     umumiy_summ = umumiy_summ + maxsulotlar.get(maxsulot)*maxsulot_xajmi
# # # # # # # # # # # # #     maxsulot = input("Maxsulotni nomini kiriting")
# # # # # # # # # # # # # else:
# # # # # # # # # # # # #     print("Umumuy summa:  " + str(umumiy_summ)) 
# # # # # # # # # # # # # a, b = 0, 1


# # # # # # # # # # # # n = int(input("50gacha son kiriting: "))
# # # # # # # # # # # # a = 0
# # # # # # # # # # # # b = 1
# # # # # # # # # # # # count = 0
# # # # # # # # # # # # temp = 0
# # # # # # # # # # # # while temp < n :
# # # # # # # # # # # #     temp = a + b
# # # # # # # # # # # #     a = b
# # # # # # # # # # # #     b = temp
# # # # # # # # # # # #     print(temp)

# # # # # # # # # # # # def fibonacci(n):
# # # # # # # # # # # #     fib_sequence = [0, 1]
# # # # # # # # # # # #     while fib_sequence[-1] <= n:
# # # # # # # # # # # #         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
# # # # # # # # # # # #     return fib_sequence[:-1]

# # # # # # # # # # # # n = int(input("Fibonacci uchun nechchigacha bo'lgan raqam kerak? "))
# # # # # # # # # # # # result = fibonacci(n)
# # # # # # # # # # # # print(result)

# # # # # # # # # # # # mevalar = ('olma', 'anor', 'sok')

# # # # # # # # # # # # meva_nomi = input('Meva nomini ayting: ')

# # # # # # # # # # # # if meva_nomi in mevalar:
# # # # # # # # # # # #     print('okay')
# # # # # # # # # # # # else:
# # # # # # # # # # # #     print('uzur')\

# # # # # # # # # # # # sanoq = 0
# # # # # # # # # # # # while(sanoq <= 100000000):
# # # # # # # # # # # #     print("Assalomu Alekum")
# # # # # # # # # # # #     continue
# # # # # # # # # # # #     sanoq += 1
# # # # # # # # # # # # for i in range(0, 1000000):
# # # # # # # # # # # #     print(i)

# # # # # # # # # # # # taxminiy_raqam = random.randint(1, 1000000)
# # # # # # # # # # # # print(taxminiy_raqam)	

# # # # # # # # # # # # import random

# # # # # # # # # # # # def tosh_qaychi_qogoz():
# # # # # # # # # # # #     while True:
# # # # # # # # # # # #         variants = ['tosh', 'qaychi', 'qog\'oz']
# # # # # # # # # # # #         tanla = input("Tosh, qaychi, qog'oz o'yini uchun tanlang (tosh/qaychi/qog'oz) yoki 'exit' deb yozing: ").lower()
        
# # # # # # # # # # # #         if tanla == 'exit':
# # # # # # # # # # # #             print("O'yin tugadi. Rahmat!")
# # # # # # # # # # # #             break

# # # # # # # # # # # #         if tanla not in variants:
# # # # # # # # # # # #             print("Noto'g'ri tanlov. Boshqattan kiriting.")
# # # # # # # # # # # #             continue

# # # # # # # # # # # #         foydalanuvchi_variant = variants.index(tanla)
# # # # # # # # # # # #         kompyuter_variant = random.randint(0, 2)
        
# # # # # # # # # # # #         print(f"San {variants[foydalanuvchi_variant]} tanladin:")
# # # # # # # # # # # #         print(f"AI {variants[kompyuter_variant]} tanladi:")
        
# # # # # # # # # # # #         if foydalanuvchi_variant == kompyuter_variant:
# # # # # # # # # # # #             print("Qaytaddan o'yna:) ")
# # # # # # # # # # # #         elif (foydalanuvchi_variant - kompyuter_variant) % 3 == 1:
# # # # # # # # # # # #             print("yutdik !!!!")
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             print("AI Yutdi :(")


# # # # # # # # # # tosh_qaychi_qogoz()
# # # # # # # # # def tictactoe():
# # # # # # # # #     board = [' ' for _ in range(9)]  

# # # # # # # # #     def print_board():
# # # # # # # # #         print(f"{board[0]} | {board[1]} | {board[2]}")
# # # # # # # # #         print("--+---+--")
# # # # # # # # #         print(f"{board[3]} | {board[4]} | {board[5]}")
# # # # # # # # #         print("--+---+--")
# # # # # # # # #         print(f"{board[6]} | {board[7]} | {board[8]}")

# # # # # # # # #     def check_winner():
# # # # # # # # #         for i in range(3):
# # # # # # # # #             if board[i] == board[i + 3] == board[i + 6] != ' ':
# # # # # # # # #                 return True
# # # # # # # # #             if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] != ' ':
# # # # # # # # #                 return True

# # # # # # # # #         if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
# # # # # # # # #             return True

# # # # # # # # #         return False

# # # # # # # # #     def is_board_full():
# # # # # # # # #         return ' ' not in board

# # # # # # # # #     def is_valid_move(move):
# # # # # # # # #         return 0 <= move < 9 and board[move] == ' '

# # # # # # # # #     def play():
# # # # # # # # #         current_player = 'X'

# # # # # # # # #         while True:
# # # # # # # # #             print_board()

# # # # # # # # #             move = int(input(f"O'yinchilar {current_player} qatnashish uchun joy tanlang (0-8): "))

# # # # # # # # #             if is_valid_move(move):
# # # # # # # # #                 board[move] = current_player

# # # # # # # # #                 if check_winner():
# # # # # # # # #                     print_board()
# # # # # # # # #                     print(f"{current_player} g'alaba qozondi! Tabriklaymiz!")
# # # # # # # # #                     break
# # # # # # # # #                 elif is_board_full():
# # # # # # # # #                     print_board()
# # # # # # # # #                     print("Durrang! Durrang! Durrang! Durrang!")
# # # # # # # # #                     break

# # # # # # # # #                 current_player = 'O' if current_player == 'X' else 'X'
# # # # # # # # #             else:
# # # # # # # # #                 print("Noto'g'ri harakat! Qayta urinib ko'ring.")
    
# # # # # # # # #     play()

# # # # # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # # # # #     tictactoe()
# # # # # # # # # # # # # lamp_nomi = "led"
# # # # # # # # # # # # # lampa_kuchlanishi = 12.3
# # # # # # # # # # # # # lampa_rangi = "led"



# # # # # # # # # # # # # class moshina:
# # # # # # # # # # # # #     dvigitel = 1.6
# # # # # # # # # # # # #     rangi = "oq"
# # # # # # # # # # # # #     balon_soni = 4

# # # # # # # # # # # # # obyekt = moshina()


# # # # # # # # # #############################################################################################################################


# # # # # # # # # # # # class oquvchi:
# # # # # # # # # # # #     def __init__(self, name , surname , age , weight , clothes):
# # # # # # # # # # # #         self.__name = name
# # # # # # # # # # # #         self.__surname = surname
# # # # # # # # # # # #         self.__age = age
# # # # # # # # # # # #         self.__weight = weight
# # # # # # # # # # # #         self.__clothes = clothes
        
# # # # # # # # # # # # #setter
# # # # # # # # # # # # def set_name(self, name):
# # # # # # # # # # # #     self.__name = name

# # # # # # # # # # # # def set_surname(self, surname):
# # # # # # # # # # # #     self.__surname = surname

# # # # # # # # # # # # def set_age(self, age):
# # # # # # # # # # # #     self.__age = age

# # # # # # # # # # # # def set_weight(self, weight):
# # # # # # # # # # # #     self.__weight = weight

# # # # # # # # # # # # def set_clothes(self, clothes):
# # # # # # # # # # # #     self.__clothes = clothes

# # # # # # # # # # # # #getter
    
# # # # # # # # # # # # def get_name(self):
# # # # # # # # # # # #     return self.__name

# # # # # # # # # # # # def get_surname(self): 
# # # # # # # # # # # #     return self.__surname

# # # # # # # # # # # # def get_age(self):
# # # # # # # # # # # #     return self.__age

# # # # # # # # # # # # def get_weight(self):
# # # # # # # # # # # #     return self.__weight

# # # # # # # # # # # # def get_clothes(self):
# # # # # # # # # # # #     return self.__clothes

# # # # # # # # # # # # def start(self):
# # # # # # # # # # # #     print()


# # # # # # # # # # # class oquvchi:
# # # # # # # # # # #     def __init__(self, mijoz,5 username , ID):
# # # # # # # # # # #          self.__mijoz = mijoz
# # # # # # # # # # #          self.__
# # # # # # # # # # #          self.__age = age
# # # # # # # # # # #          self.__weight = weight
# # # # # # # # # # #          self.__clothes = clothes

# # # # # # # # # # class BNK:
# # # # # # # # # #      def __init__(self, balance):
# # # # # # # # # #         self.balance = balance

# # # # # # # # # #      def check_balance(self):
# # # # # # # # # #         return self.balance

# # # # # # # # # #      def deposit(self, amount):
# # # # # # # # # #         self.balance += amount
# # # # # # # # # #         return f"Deposit of {amount} successful. New balance is {self.balance}"

# # # # # # # # # #      def withdraw(self, amount):
# # # # # # # # # #         if self.balance >= amount:
# # # # # # # # # #             self.balance -= amount
# # # # # # # # # #             return f"Withdrawal of {amount} successful. New balance is {self.balance}"
# # # # # # # # # #         else:
# # # # # # # # # #             return "money left"


# # # # # # # # # # atm = BNK(1000) 
# # # # # # # # # # print(atm.check_balance())  
# # # # # # # # # # print(atm.deposit(500))  
# # # # # # # # # # print(atm.withdraw(200))  
# # # # # # # # # # print(atm.()) 
# # # # # # # # # # print(atm.wicheck_balancethdraw(1500))  

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #




# # # # # # # # # # a = 1
# # # # # # # # # # b = 4

# # # # # # # # # # if ( a + b == 3):
# # # # # # # # # #     print('hammasi yoyida')
# # # # # # # # # # else: {
# # # # # # # # # #     print('xatolik')
# # # # # # # # # # }


# # # # # # # # # # class Taxi:
# # # # # # # # # #     def __init__(self, name, location):
# # # # # # # # # #         self.name = name
# # # # # # # # # #         self.location = location

# # # # # # # # # #     def move(self, new_location):
# # # # # # # # # #         print(f"{self.name} joyidan {self.location} dan {new_location} ga harakat qilmoqda.")
# # # # # # # # # #         self.location = new_location

# # # # # # # # # # class TaxiService:
# # # # # # # # # #     def __init__(self):
# # # # # # # # # #         self.taxis = {}

# # # # # # # # # #     def add_taxi(self, taxi):
# # # # # # # # # #         self.taxis[taxi.name] = taxi

# # # # # # # # # #     def request_taxi(self, name, destination):
# # # # # # # # # #         if name in self.taxis:
# # # # # # # # # #             print(f"{name} avtomobili sizni {destination} ga olib boradi.")
# # # # # # # # # #             self.taxis[name].move(destination)
# # # # # # # # # #         else:
# # # # # # # # # #             print(f"Kechirasiz, {name} nomli avtomobil topilmadi.")

# # # # # # # # # # # Test qismi
# # # # # # # # # # if __name__ == "__main__":
# # # # # # # # # #     taxi1 = Taxi("Taxi #1", "A")
# # # # # # # # # #     taxi2 = Taxi("Taxi #2", "B")
# # # # # # # # # #     taxi3 = Taxi("Taxi #3", "C")

# # # # # # # # # #     service = TaxiService()
# # # # # # # # # #     service.add_taxi(taxi1)
# # # # # # # # # #     service.add_taxi(taxi2)
# # # # # # # # # #     service.add_taxi(taxi3)

# # # # # # # # # #     service.request_taxi("Taxi #1", "D")
# # # # # # # # # #     service.request_taxi("Taxi #2", "E")
# # # # # # # # # #     service.request_taxi("Taxi #4", "F")  

# # # # # # # # # from itertools import combinations_with_replacement

# # # # # # # # # def kupyura_combination(total_sum, kupyura_soni):
# # # # # # # # #     # Mavjud kupyura qiymatlari
# # # # # # # # #     kupyuralar = [10, 20, 50, 100]
    
# # # # # # # # #     possible_combinations = combinations_with_replacement(kupyuralar, kupyura_soni)
    
# # # # # # # # #     valid_combinations = [combo for combo in possible_combinations if sum(combo) == total_sum]
    
# # # # # # # # #     return valid_combinations

# # # # # # # # # kombinatsiyalar = kupyura_combination(500, 10)

# # # # # # # # # if kombinatsiyalar:
# # # # # # # # #     for idx, combo in enumerate(kombinatsiyalar, 1):
# # # # # # # # #         print(f"{idx}-kombinatsiya: {combo}")
# # # # # # # # # # else:
# # # # # # # # # #     print("Mos kombinatsiya topilmadi.")

# # # # # # # # # from itertools import combinations_with_replacement

# # # # # # # # # def kupyura_combination(total_sum, kupyura_soni):
# # # # # # # # #     # Mavjud kupyura qiymatlari
# # # # # # # # #     kupyuralar = [10, 20, 50, 100]
    
# # # # # # # # #     possible_combinations = combinations_with_replacement(kupyuralar, kupyura_soni)
    
# # # # # # # # #     valid_combinations = [combo for combo in possible_combinations if sum(combo) == total_sum]
    
# # # # # # # # #     return valid_combinations

# # # # # # # # # # Foydalanuvchi inputi
# # # # # # # # # total_sum = int(input("Summani kiriting: "))
# # # # # # # # # kupyura_soni = int(input("Kupyura sonini kiriting: "))

# # # # # # # # # kombinatsiyalar = kupyura_combination(total_sum, kupyura_soni)

# # # # # # # # # if kombinatsiyalar:
# # # # # # # # #     for idx, combo in enumerate(kombinatsiyalar, 1):
# # # # # # # # #         print(f"{idx}-kombinatsiya: {combo}")
# # # # # # # # # else:
# # # # # # # # #     print("Mos kombinatsiya topilmadi.")

# # # # # # # # # from itertools import combinations_with_replacement
# # # # # # # # #
# # # # # # # # # def kupyura_combination(total_sum, kupyura_soni):
# # # # # # # # #     kupyuralar = [1, 2, 5, 10, 20, 50, 100]
# # # # # # # # #
# # # # # # # # #     possible_combinations = combinations_with_replacement(kupyuralar, kupyura_soni)
# # # # # # # # #
# # # # # # # # #     valid_combinations = [combo for combo in possible_combinations if sum(combo) == total_sum]
# # # # # # # # #
# # # # # # # # #     return valid_combinations
# # # # # # # # #
# # # # # # # # # total_sum = int(input("Summani kiriting: "))
# # # # # # # # # kupyura_soni = int(input("Kupyura sonini kiriting: "))
# # # # # # # # #
# # # # # # # # # kombinatsiyalar = kupyura_combination(total_sum, kupyura_soni)
# # # # # # # # #
# # # # # # # # # if kombinatsiyalar:
# # # # # # # # #     print(f"1-kombinatsiya: {kombinatsiyalar[0]}")
# # # # # # # # # else:
# # # # # # # # #     print("Mos kombinatsiya topilmadi.")
# # # # # # # # # class Car:
# # # # # # # # #     def __init__(self, brand, color, year):
# # # # # # # # #         self.brand = brand
# # # # # # # # #         self.color = color
# # # # # # # # #         self.year = year
# # # # # # # # #         self.speed = 0
# # # # # # # # #
# # # # # # # # #     def accelerate(self, amount):
# # # # # # # # #         self.speed += amount
# # # # # # # # #         print(f"Gaz bosildi! Yangi tezlik: {self.speed} km/soat")
# # # # # # # # #
# # # # # # # # #     def brake(self, amount):
# # # # # # # # #         if self.speed - amount < 0:
# # # # # # # # #             self.speed = 0
# # # # # # # # #         else:
# # # # # # # # #             self.speed -= amount
# # # # # # # # #         print(f"Tormoz bosildi! Yangi tezlik: {self.speed} km/soat")
# # # # # # # # #
# # # # # # # # #     def get_info(self):
# # # # # # # # #         return f"Brend: {self.brand}, Rang: {self.color}, Yil: {self.year}, Tezlik: {self.speed} km/soat"
# # # # # # # # #
# # # # # # # # # my_car = Car(brand="BMW", color="Qora", year=1998)
# # # # # # # # #
# # # # # # # # # print(my_car.get_info())
# # # # # # # # #
# # # # # # # # # my_car.accelerate(30)
# # # # # # # # # my_car.accelerate(20)
# # # # # # # # #
# # # # # # # # # my_car.brake(20)
# # # # # # # # # my_car.brake(30)
# # # # # # # # #
# # # # # # # # # print(my_car.get_info()


# # # # # # # # ################################################################################################################################################################################################################


# # # # # # # # # import numpy as np
# # # # # # # # # # a = np.arrange (1,10)
# # # # # # # # # # print(a)

# # # # # # # # # # b =np.array([1,4,5,8])
# # # # # # # # # # print(b)

# # # # # # # # # # import numpy as np
# # # # # # # # # # array = np.array([1, 2, 3])
# # # # # # # # # # print(array)

# # # # # # # # # # import random
# # # # # # # # # # c=np.array([random.randint(-10,10) for x in range (0,10)])
# # # # # # # # # # print(c)
# # # # # # # # # # a= np.linspace(1,10,7)
# # # # # # # # # # print(a)
# # # # # # # # # import random
# # # # # # # # # # a=np.ones((10000),int)
# # # # # # # # # # print(a)
# # # # # # # # # a=np.ones((5),int)
# # # # # # # # # print(a)

# # # # # # # # ######################################################################################


# # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # import numpy as np
# # # # # # # # # xpoint = np.array([1,8,6,3,4])
# # # # # # # # # ypoint = np.array([3,9,10,9])

# # # # # # # # # plt.plot(xpoint, ypoint)
# # # # # # # # # plt.show()
# # # # # # # # ##########################################################################################


# # # # # # # # # import matplotlib.pyplot as plt
# # # # # # # # # import numpy as np

# # # # # # # # # y= np.array([35,25,25,15])
# # # # # # # # # mylabels = ("Appples", "Bananas", "cherries", "Dates")
# # # # # # # # # plt.pie(y, labels = mylabels, startangle=90)
# # # # # # # # # plt.show()
# # # # # # # # #########################################################
# # # # # # # # # import numpy as np
# # # # # # # # # arr = np.array([[1,2,3,4],[5,6,7,8]])
# # # # # # # # # print(arr.shape)
# # # # # # # # #################################################

# # # # # # # # # n = 6
# # # # # # # # # for i in range(0, n):
# # # # # # # # #     print(i)
# # # # # # # # ################################################

# # # # # # # # # new = ["A", "G"]
# # # # # # # # # user_input = input("Harf kiriting: ") 
# # # # # # # # # if user_input.upper() in new:
# # # # # # # # #     print("Good")
# # # # # # # # # else:
# # # # # # # # #     print("Try again")

# # # # # # # # # import cv2

# # # # # # # # # # Read the image
# # # # # # # # # image = cv2.imread(r"D:\games\mm\kla.jpg")

# # # # # # # # # if image is None:
# # # # # # # # #     print("Error loading image.")
# # # # # # # # # else:
# # # # # # # # #     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # # # # # # # #     edges = cv2.Canny(gray, 50, 150)   
# # # # # # # # #     contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # # # # # # # #     cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
# # # # # # # # #     cv2.imshow('Contours', image)
# # # # # # # # #     cv2.waitKey(0)
# # # # # # # # #     cv2.destroyAllWindows()
    



# # # # # # # # #####################################################################################

# # # # # # # # # def f(y):
# # # # # # # # #     if y < 0:
# # # # # # # # #         return -1
# # # # # # # # #     elif y == 0:
# # # # # # # # #         return 0
# # # # # # # # #     else:
# # # # # # # # #         return 1


# # # # # # # # # def RootsCount(a, b, c):
    
# # # # # # # # #     D = b**2 - 4*a*c
    
# # # # # # # # #     if D > 0:
# # # # # # # # #         return 2  # 2 ta haqiqiy ildiz
# # # # # # # # #     elif D == 0:
# # # # # # # # #         return 1  # 1 ta haqiqiy ildiz
# # # # # # # # #     else:
# # # # # # # # #         return 0  # Haqiqiy ildiz yo'q


# # # # # # # # # def CircleS(r):
# # # # # # # # #     return 3.14 * r**2

# # # # # # # # # radiuslar = [3, 5, 7]

# # # # # # # # # for r in radiuslar:
# # # # # # # # #     yuzasi = CircleS(r)
# # # # # # # # #     print(f"r = {r} bo'lgan doiraning yuzasi: {yuzasi:.2f}"


# # # # # # # # # class TappleError(Exception):
# # # # # # # # #     pass

# # # # # # # # # def check_value(value):
# # # # # # # # #     if value != "tapple":
# # # # # # # # #         raise TappleError("Error: Bu 'tapple' emas!")
# # # # # # # # #     return "Bu 'tapple'!"

# # # # # # # # # try:
# # # # # # # # #     check_value("apple") 
# # # # # # # # # except TappleError as e:
# # # # # # # # #     print(e)
# # # # # # # # # Tuple yaratish
# # # # # # # # # my_tuple = (1, 2, 3, "salom", True)

# # # # # # # # # # Tuple'ni list'ga aylantirish va o'zgartirish

# # # # # # # # # my_tuple[1] = "o'zgartirilgan qiymat"

# # # # # # # # # # List'ni yana tuple'ga aylantirish
# # # # # # # # # my_tuple = tuple(my_tuple)
# # # # # # # # # print(my_tuple)

# # # # # # # # person = {
# # # # # # # #     "name": "Akbarali",
# # # # # # # #     "age": 25,
# # # # # # # #     "city": "Tashkent"
# # # # # # # # }
# # # # # # # # car = {
# # # # # # # #     "brand": "Toyota",
# # # # # # # #     "model": "Corolla",
# # # # # # # #     "year": 2020
# # # # # # # # }

# # # # # # # # book = {
# # # # # # # #     "title": "Python Programming",
# # # # # # # #     "author": "John Doe",
# # # # # # # #     "pages": 320
# # # # # # # # }
# # # # # # # # product = {
# # # # # # # #     "name": "Laptop",
# # # # # # # #     "brand": "Dell",
# # # # # # # #     "price": 1500
# # # # # # # # }

# # # # # # # # student = {
# # # # # # # #     "name": "Ali",
# # # # # # # #     "grade": "A",
# # # # # # # #     "major": "Computer Science"
# # # # # # # # }

# # # # # # # # job = {
# # # # # # # #     "title": "Software Engineer",
# # # # # # # #     "company": "Google",
# # # # # # # #     "location": "California"
# # # # # # # # }
# # # # # # # # restaurant = {
# # # # # # # #     "name": "Burger House",
# # # # # # # #     "type": "Fast Food",
# # # # # # # #     "rating": 4.5
# # # # # # # # }

# # # # # # # # house = {
# # # # # # # #     "type": "Apartment",
# # # # # # # #     "rooms": 3,
# # # # # # # #     "price": 75000
# # # # # # # # }

# # # # # # # # movie = {
# # # # # # # #     "title": "Inception",
# # # # # # # #     "director": "Christopher Nolan",
# # # # # # # #     "year": 2010
# # # # # # # # }

# # # # # # # # song = {
# # # # # # # #     "title": "Bohemian Rhapsody",
# # # # # # # #     "artist": "Queen",
# # # # # # # #     "duration": "5:55"
# # # # # # # # }


# # # # # # # # class car:
# # # # # # # #     engine = "v9 Turbo"
# # # # # # # #     model = "impala"
# # # # # # # #     brand = "chevroler"

# # # # # # # # # first = car()
# # # # # # # # # second = car()
# # # # # # # # # third = car()
# # # # # # # # # print(first.engine)
# # # # # # # # # print(second.model)

# # # # # # # # def  show_info():
# # # # # # # #     return f"mishina"
# # # # # # # # first = car()
# # # # # # # # print(first.show_info())

# # # # # # # class car:
# # # # # # #     model = "impala"
# # # # # # #     fuel = "gaz"
    
# # # # # # # first = car()
# # # # # # # first.model = "impala"
# # # # # # # first.new = "qiymat"
# # # # # # # setattr(car,"yangi","value")
# # # # # # # thirt = car()
# # # # # # # print(hasattr(thirt,"yangi2"))
# # # # # # # # delattr(thirt,"model")
# # # # # # # del first.model

# # # # # class User: 
# # # # #     def __init__(self,LOGIN, password):
# # # # #         self.LOGIN = LOGIN
# # # # #         self.password = password

# # # # # class circle:
# # # # #     def __init__(self,r):
# # # # #         self.r = r
# # # # #     def surface(self):
# # # # #             return 2*3.14*self.r**2

# # # # # class Square:
# # # # #     def __init__(self,x,y):
# # # # #         self.x = x
# # # # #         self.y = y
# # # # #     def surface(self):
# # # # #         return self.x*self.y
# # # # # doira = circle(4)
# # # # # doira2 = circle(3)
# # # # # turt_burchak = Square(3,4)
# # # # # turt_burchak2 = Square(4,5)
# # # # # sum = (doira, doira2, turt_burchak, turt_burchak2)
# # # # # for i in sum:
# # # # #     print(i.surface())
# # # # # from abc import ABC, abstractmethod

# # # # # class Avtomobil(ABC):
# # # # #     def __init__(self, model, rang):
# # # # #         self.model = model
# # # # #         self.rang = rang
# # # # #     @abstractmethod
# # # # #     def yurgizish(self):
# # # # #         pass

# # # # #     @abstractmethod
# # # # #     def toxtatish(self):
# # # # #         pass

# # # # # class Sedan(Avtomobil):
# # # # #     def yurgizish(self):
# # # # #         print(f"{self.model} avtomobili yurgizildi!")

# # # # #     def toxtatish(self):
# # # # #         print(f"{self.model} avtomobili to'xtatildi!")

# # # # # class YukAvtomobili(Avtomobil):
# # # # #     def yurgizish(self):
# # # # #         print(f"{self.model} yuk mashinasi yurgizildi!")

# # # # #     def toxtatish(self):    
# # # # #         print(f"{self.model} yuk mashinasi to'xtatildi!")

# # # # # avto1 = Sedan("Toyota Camry", "Oq")
# # # # # avto2 = YukAvtomobili("KamAZ", "Qora")

# # # # # avto1.yurgizish()   
# # # # # avto2.toxtatish()  

# # # # # rows =5 
# # # # # for i in range(1, rows + 1):
# # # # #     for j in range(1, i +1):
# # # # #         print("*", end=" ")
# # # # #     print()


# # # # # import numpy as np

# # # # # matrix = np.arange(1, 26).reshape(5, 5)

# # # # # numbers_to_sum = [1, 7, 5, 9, 13, 17, 19, 21, 25]

# # # # # sum_of_selected_numbers = sum(num for row in matrix for num in row if num in numbers_to_sum)

# # # # # print("Tanlangan sonlar yig'indisi:", sum_of_selected_numbers)

# # # # # #####################################################################################################
# # # # # matrix = [
# # # # #     [1, 2, 3, 4, 5],
# # # # #     [6, 7, 8, 9, 10],
# # # # #     [11, 12, 13, 14, 15],
# # # # #     [16, 17, 18, 19, 20],
# # # # #     [21, 22, 23, 24, 25]
# # # # # ]

# # # # # numbers_to_sum = [1, 7, 5, 9, 13, 17, 19, 21, 25]

# # # # # sum_of_selected_numbers = 0

# # # # # for row in matrix:
# # # # #     for num in row:
# # # # #         if num in numbers_to_sum:
# # # # #             sum_of_selected_numbers += num

# # # # # print("Tanlangan sonlar yig'indisi:", sum_of_selected_numbers)


# # # # # keypad = {
# # # # #     '1': '.,?!',
# # # # #     '2': 'abc',
# # # # #     '3': 'def',
# # # # #     '4': 'ghi',
# # # # #     '5': 'jkl',
# # # # #     '6': 'mno',
# # # # #     '7': 'pqrs',
# # # # #     '8': 'tuv',
# # # # #     '9': 'wxyz',
# # # # #     '0': ' ',
# # # # # }

# # # # # def count_keypresses(message):
# # # # #     count = 0
# # # # #     for char in message.lower():  
# # # # #         for key, letters in keypad.items():
# # # # #             if char in letters:
# # # # #                 count += letters.index(char) + 1  
# # # # #                 break
# # # # #     return count

# # # # # message = input("SMS xabarni kiriting: ")
# # # # # keypress_count = count_keypresses(message)
# # # # # print(f"Xabarni yozish uchun {keypress_count} marta tugmalar bosilishi kerak.")


# # # # # a_list = []
# # # # # for ozgar in range(5):
# # # # #     b_list=[]
# # # # #     for k in range(4):
# # # # #         if k == 0 or  ozgar ==4 or ozgar ==0  or k ==3 or ozgar==2 :
# # # # #             b_list.append("#")
# # # # #         else:
# # # # #             b_list.append("*")
# # # # #     print(b_list)




# # # # # a_list =[]
# # # # # for ozgar in range(5):
# # # # #     b_list=[]
# # # # #     for k in range(5):
# # # # #         if ozgar ==0 or ozgar ==2 or ozgar ==4 or k==0 or k==2 or k==4: 
# # # # #             b_list.append("#")
# # # # #         else:
# # # # #             b_list.append("0")
# # # # #     print(b_list)

# # # # # a_list = []
# # # # # for ozgar in range(5):
# # # # #     b_list = []
# # # # #     for k in range(5):
# # # # #         if  k ==2:  
# # # # #             b_list.append("#")
         
            
# # # # #         else:  
# # # # #             b_list.append("0")
# # # # #     a_list.append(b_list)
# # # # #     print(b_list)



# # # # #imputni outpatni organish


# # # # #fibanachi
# # # # # n = int(input("Nechta Fibonacci soni kerak? "))

# # # # # a, b = 0, 1
# # # # # for _ in range(n):
# # # # #     print(a, end=" ")
# # # # #     a, b = b, a + b

    


# # # # # def fibonacci(n):
# # # # #     a, b = 0, 1
# # # # #     for _ in range(n):
# # # # #         a, b = b, a + b
# # # # #     return a

# # # # # n = int(input("son et: "))
# # # # # if n < 0:
# # # # #     print("minus son ")
# # # # # else:
# # # # #     print(f"{n} javob: {fibonacci(n)}")


# # # # import pygame
# # # # import time
# # # # import random

# # # # # O'yin uchun ranglar
# # # # white = (255, 255, 255)
# # # # yellow = (255, 255, 102)
# # # # black = (0, 0, 0)
# # # # red = (213, 50, 80)
# # # # green = (0, 255, 0)
# # # # blue = (50, 153, 213)

# # # # # O'yin oynasi o'lchami
# # # # dis_width = 800
# # # # dis_height = 600

# # # # # Pygame-ni ishga tushirish
# # # # pygame.init()

# # # # # O'yin oynasi yaratish
# # # # dis = pygame.display.set_mode((dis_width, dis_height))
# # # # pygame.display.set_caption('Snake Game')

# # # # clock = pygame.time.Clock()

# # # # snake_block = 10
# # # # snake_speed = 15

# # # # font_style = pygame.font.SysFont("bahnschrift", 25)
# # # # score_font = pygame.font.SysFont("comicsansms", 35)


# # # # def our_snake(snake_block, snake_list):
# # # #     for x in snake_list:
# # # #         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# # # # def message(msg, color):
# # # #     mesg = font_style.render(msg, True, color)
# # # #     dis.blit(mesg, [dis_width / 6, dis_height / 3])


# # # # def gameLoop():  # O'yin sikli
# # # #     game_over = False
# # # #     game_close = False

# # # #     x1 = dis_width / 2
# # # #     y1 = dis_height / 2

# # # #     x1_change = 0
# # # #     y1_change = 0

# # # #     snake_List = []
# # # #     Length_of_snake = 1

# # # #     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
# # # #     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

# # # #     while not game_over:

# # # #         while game_close:
# # # #             dis.fill(blue)
# # # #             message("You lost! Press Q-Quit or C-Play Again", red)
# # # #             pygame.display.update()

# # # #             for event in pygame.event.get():
# # # #                 if event.type == pygame.KEYDOWN:
# # # #                     if event.key == pygame.K_q:
# # # #                         game_over = True
# # # #                         game_close = False
# # # #                     if event.key == pygame.K_c:
# # # #                         gameLoop()

# # # #         for event in pygame.event.get():
# # # #             if event.type == pygame.QUIT:
# # # #                 game_over = True
# # # #             if event.type == pygame.KEYDOWN:
# # # #                 if event.key == pygame.K_LEFT:
# # # #                     x1_change = -snake_block
# # # #                     y1_change = 0
# # # #                 elif event.key == pygame.K_RIGHT:
# # # #                     x1_change = snake_block
# # # #                     y1_change = 0
# # # #                 elif event.key == pygame.K_UP:
# # # #                     y1_change = -snake_block
# # # #                     x1_change = 0
# # # #                 elif event.key == pygame.K_DOWN:
# # # #                     y1_change = snake_block
# # # #                     x1_change = 0

# # # #         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
# # # #             game_close = True
# # # #         x1 += x1_change
# # # #         y1 += y1_change
# # # #         dis.fill(blue)
# # # #         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
# # # #         snake_Head = []
# # # #         snake_Head.append(x1)
# # # #         snake_Head.append(y1)
# # # #         snake_List.append(snake_Head)
# # # #         if len(snake_List) > Length_of_snake:
# # # #             del snake_List[0]

# # # #         for x in snake_List[:-1]:
# # # #             if x == snake_Head:
# # # #                 game_close = True

# # # #         our_snake(snake_block, snake_List)

# # # #         pygame.display.update()

# # # #         if x1 == foodx and y1 == foody:
# # # #             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
# # # #             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
# # # #             Length_of_snake += 1

# # # #         clock.tick(snake_speed)

# # # #     pygame.quit()
# # # #     quit()


# # # # gameLoop()

# # # import pygame
# # # import time
# # # import random

# # # # O'yin uchun ranglar
# # # white = (255, 255, 255)
# # # yellow = (255, 255, 102)
# # # black = (0, 0, 0)
# # # red = (213, 50, 80)
# # # green = (0, 255, 0)
# # # blue = (50, 153, 213)

# # # # O'yin oynasi o'lchami
# # # dis_width = 800
# # # dis_height = 600

# # # # Pygame-ni ishga tushirish
# # # pygame.init()

# # # # O'yin oynasi yaratish
# # # dis = pygame.display.set_mode((dis_width, dis_height))
# # # pygame.display.set_caption('Snake Game')

# # # clock = pygame.time.Clock()

# # # snake_block = 5
# # # snake_speed = 100

# # # font_style = pygame.font.SysFont("bahnschrift", 25)
# # # score_font = pygame.font.SysFont("comicsansms", 35)


# # # def our_snake(snake_block, snake_list):
# # #     for x in snake_list:
# # #         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


# # # def draw_food(food_positions, food_color, block_size):
# # #     for food in food_positions:
# # #         pygame.draw.rect(dis, food_color, [food[0], food[1], block_size, block_size])


# # # def message(msg, color):
# # #     mesg = font_style.render(msg, True, color)
# # #     dis.blit(mesg, [dis_width / 6, dis_height / 3])


# # # def gameLoop():  # O'yin sikli
# # #     game_over = False
# # #     game_close = False

# # #     x1 = dis_width / 2
# # #     y1 = dis_height / 2

# # #     x1_change = 0
# # #     y1_change = 0

# # #     snake_List = []
# # #     Length_of_snake = 1

# # #     # Tasodifiy joylashgan oziq-ovqatlar ro'yxati
# # #     food_positions = [
# # #         [round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
# # #          round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0]
# # #         for _ in range(1000)  # 5 ta oziq-ovqat yaratamiz
# # #     ]

# # #     while not game_over:

# # #         while game_close:
# # #             dis.fill(blue)
# # #             message("You lost! Press Q-Quit or C-Play Again", red)
# # #             pygame.display.update()

# # #             for event in pygame.event.get():
# # #                 if event.type == pygame.KEYDOWN:
# # #                     if event.key == pygame.K_q:
# # #                         game_over = True
# # #                         game_close = False
# # #                     if event.key == pygame.K_c:
# # #                         gameLoop()

# # #         for event in pygame.event.get():
# # #             if event.type == pygame.QUIT:
# # #                 game_over = True
# # #             if event.type == pygame.KEYDOWN:
# # #                 if event.key == pygame.K_LEFT:
# # #                     x1_change = -snake_block
# # #                     y1_change = 0
# # #                 elif event.key == pygame.K_RIGHT:
# # #                     x1_change = snake_block
# # #                     y1_change = 0
# # #                 elif event.key == pygame.K_UP:
# # #                     y1_change = -snake_block
# # #                     x1_change = 0
# # #                 elif event.key == pygame.K_DOWN:
# # #                     y1_change = snake_block
# # #                     x1_change = 0

# # #         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
# # #             game_close = True
# # #         x1 += x1_change
# # #         y1 += y1_change
# # #         dis.fill(blue)

# # #         # Nagachalarni chizish
# # #         draw_food(food_positions, green, snake_block)

# # #         snake_Head = []
# # #         snake_Head.append(x1)
# # #         snake_Head.append(y1)
# # #         snake_List.append(snake_Head)
# # #         if len(snake_List) > Length_of_snake:
# # #             del snake_List[0]

# # #         for x in snake_List[:-1]:
# # #             if x == snake_Head:
# # #                 game_close = True

# # #         our_snake(snake_block, snake_List)

# # #         pygame.display.update()

# # #         # Har bir oziq-ovqatni tekshirish
# # #         for food in food_positions[:]:
# # #             if x1 == food[0] and y1 == food[1]:
# # #                 food_positions.remove(food)
# # #                 food_positions.append([
# # #                     round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
# # #                     round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
# # #                 ])
# # #                 Length_of_snake += 1

# # #         clock.tick(snake_speed)

# # #     pygame.quit()
# # #     quit()


# # # gameLoop()



# # class user:
# #     def __init__(self, name, phonne_number):
# #         self.name = name
# #         self.phonne_number = phonne_number
# # class Ticket:
# #     def __init__(self, from_, Airplay_number, to, prise, fly_number, oneway=True):
# #         self.from_ = from_
# #         self.to = to
# #         self.oneway = oneway
# #         self.prise = prise
# #         self.fly_number = fly_number
# #         self.Airplay_number = Airplay_number

# # class Passanger:
# #     def __init__(self, pessenger_name, passport_id, passager_number):
# #         self.pessenger_name = pessenger_name
# #         self.passport_id = passport_id
# #         self.passager_number = passager_number

# # super()

# # def getter(self):
# #     return f'Name: {self.name}, Phone number: {self.phonne_number}'

# class User:
#     def __init__(self, name, phone_number):
#         self.name = name
#         self.phone_number = phone_number

#     def getter(self):
#         return f"Name: {self.name}, Phone number: {self.phone_number}"


# class Ticket:
#     def __init__(self, from_, airplay_number, to, price, fly_number, oneway=True):
#         self.from_ = from_
#         self.to = to
#         self.oneway = oneway
#         self.price = price
#         self.fly_number = fly_number
#         self.airplay_number = airplay_number

#     def getter(self):
#         direction = "One-way" if self.oneway else "Round-trip"
#         return (f"From: {self.from_}, To: {self.to}, Price: ${self.price}, "
#                 f"Flight Number: {self.fly_number}, Airplane Number: {self.airplay_number}, "
#                 f"Type: {direction}")


# class Passenger:
#     def __init__(self, passenger_name, passport_id, passenger_number):
#         self.passenger_name = passenger_name
#         self.passport_id = passport_id
#         self.passenger_number = passenger_number

#     def getter(self):
#         return (f"Passenger Name: {self.passenger_name}, Passport ID: {self.passport_id}, "
#                 f"Passenger Number: {self.passenger_number}")



# # if __name__ == "__main__":

# #     user1 = User("Akbarali", "+998900123456")
# #     print(user1.getter())


# #     ticket1 = Ticket(from_="Tashkent", airplay_number="A320", to="Dubai", price=250, fly_number="TK123")
# #     print(ticket1.getter())

# #     passenger1 = Passenger("Akbarali Sh", "AA1234567", "P001")
# #     print(passenger1.getter())


# #     print(f"\nTicket for {passenger1.passenger_name}:")
# #     print(ticket1.getter())
# import time
# date_tuple = (2018, 10, 11, 2, 55, 23, 2, 40, 0)  
# timestamp = time.mktime(date_tuple)

# print(f"Unix timestamp: {timestamp}")   

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, DateTime                                                                                                                                                                                                 # type: ignore
from sqlalchemy.orm import relationship, declarative_base                                                                                                                                                                                                 # type: ignore
from sqlalchemy.ext.declarative import declarative_base                                                                                                                                                       # type: ignore
import datetime

# Create the base class for our models
Base = declarative_base()

# Define the Users table
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)  # Use hashed passwords in real implementations
    role = Column(String, nullable=False)
    
    orders = relationship('Order', back_populates='user')  # Relationship with Order

# Define the Products table
class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    
    order_details = relationship('OrderDetail', back_populates='product')  # Relationship with OrderDetail

# Define the Orders table
class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default='Pending')  # For example, Pending, Completed, etc.
    
    user = relationship('User', back_populates='orders')  # Relationship with User
    order_details = relationship('OrderDetail', back_populates='order')  # Relationship with OrderDetail

# Define the OrderDetails table (junction table between Orders and Products)
class OrderDetail(Base):
    __tablename__ = 'order_details'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    
    order = relationship('Order', back_populates='order_details')  # Relationship with Order
    product = relationship('Product', back_populates='order_details')  # Relationship with Product

# Create the SQLite engine
DATABASE_URL = "sqlite:///./test.db"  # Example using SQLite; replace with your database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
Base.metadata.create_all(bind=engine)




from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

new_product = Product(name="Milk", description="Fresh cow milk", price=2.5, stock_quantity=100)
db.add(new_product)
db.commit()  

from pydantic import BaseModel

# Pydantic model for creating a product
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock_quantity: int

# Pydantic model for creating an order
class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
 
 