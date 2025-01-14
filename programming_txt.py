

# # {nima uchun pydantic kerak}

# # validatsiya : malumotlar togriligini tekshiradi
# # konvertatsiya : Malumotlarni keraklik formatga avtomatik ogiradi
# # Tushunarlik xatoalr: Xatolarni aniq va tushunarlik shaklda beradi 
# # Json_va_boshqa_farmatlar_bilan_ishlash : Malumotlarni JSON kabi farmatlardan yuklash va export qilish imkonini beradi



# # from pydantic import BaseModel

# # # malumotlarni modelini yaratish
# # class User(BaseModel):
# #     id: int
# #     name: str
# #     email: str                                  
# #     age: int 

# # # Modelni ishalatish:
# # user_data ={"id":1,"name":"Ali", "email":"ali@exaple.com", "age":25  }
# # user =User(**user_data)

# # print (user)
# # print (user.name)

# # Pydantic dan foydalanib, validatsiya va konvertatsiya ishlash imkonini beradi
# # sinf Diagrammalri
# # Tzimning classlari va ular orasidagi munosabatlarni ko'rsatish orqalik umumiy ma"lumotlar beradi. Class diagrammalari statik Ular o'zaro ta"sir qiladigan narsalarni namoish etadi va o'zaro tasir qilingan


# # Class faqt kod uchun emas
# # class holatlarinitushunchasini ifodalaydi
# # class holatlani va xatti xarakatni ifodalaydi
# # har bir xususiyatni turi bor
# # class nomi majburiy malumotdir`1`



# #Class bu uch qisimga ega bolingat tortburchak 
# # class nomi 
# # class atributlari va Class operatsiyalari
# # O;zgaruvchilar : Xususiy, Hamma, Himoyalangan, statik :ostiga chizilgan (yani sinfning barcha azollari orasida taqsimlangan)
# # Xulosa class : Ismi kursiv bilan yozilgan


# # alimpic nima python ilovalari uchun malumotlar bazasi migratsiyalarini boshqarish vositasi
# # Asosan 
# # Malumotlar bazasi strukturasini yangilash 
# # Migratsiyani otkat qilish 
# # bir necha dasturchilar uchun migratsiyali     
# # barcha migratsilarni ishga tushirish
# # `alembic upgrade head`

# # Malumotlsr BAZASINI TEKSHIRISH
# # tekushiy versiyasiniko'rish
# # `alembiccurrent`
# # migratsiyani barcha tarixi 
# # `alembic history`


# # slayd 5 fast AIPINI sozlash 
# # saravxa: fast api sozlash kodi 
# from fastapi import FASTAPI
# app = FASTAPI()   
# @app.get("?/")
# def read_root():
#     return {"massage":"hello world"}

# # ilovani yaratish 

# # foydalanuvchi auntifikatsiyasi
# # from fastapi import depends,httpeexception
# # from fastapi.security import oauth2Passwordrequest from 
# # 


products = []
orders = []

# Administrator funksiyalari
def add_product():
    name = input("Mahsulot nomi: ")
    price = int(input("Mahsulot narxi: "))
    products.append({'name': name, 'price': price})
    print(f"{name} mahsuloti qo'shildi.")

def view_orders():
    print("Buyurtmalar:")
    for order in orders:
        print(order)

# Mijoz funksiyalari
def view_products():
    print("Mahsulotlar:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product['name']} - {product['price']} so'm")

def make_order():
    view_products()
    choice = int(input("Mahsulot raqamini tanlang: ")) - 1
    quantity = int(input("Soni: "))
    selected_product = products[choice]
    orders.append({'name': selected_product['name'], 'quantity': quantity, 'total': selected_product['price'] * quantity})
    print("Buyurtma qabul qilindi.")

# Asosiy dastur
def main():
    print("NewEra Buyurtma Tizimi")
    user_type = input("Administrator (A) yoki Mijoz (M) sifatida kirish: ").lower()

    if user_type == 'a':
        while True:
            print("1. Mahsulot qo'shish\n2. Buyurtmalarni ko'rish\n3. Chiqish")
            choice = input("Tanlang: ")
            if choice == '1':
                add_product()
            elif choice == '2':
                view_orders()
            elif choice == '3':
                break
    elif user_type == 'm':
        while True:
            print("1. Mahsulotlarni ko'rish\n2. Buyurtma berish\n3. Chiqish")
            choice = input("Tanlang: ")
            if choice == '1':
                view_products()
            elif choice == '2':
                make_order()
            elif choice == '3':
                break

if __name__ == "__main__":
    main()