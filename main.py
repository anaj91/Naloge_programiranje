# Pretvarjanje iz Fahrenheitov v Celzije

# F = float(input ("Temperatura [F]:"))
# celsius = 5/9 * (F - 32)
# print(f"{F:.3g} Fahrenheitov je " f"{celsius:.4g} stopinj Celzija")

# celsius = float(input("Temperatura [C]:"))
# F = 9/5 * celsius + 32
# print(f"{celsius:.3g} stopinj Celzija je " f"{F:.3g} Fahrenheitov")
#
# def celsius(F):
#     return (F - 32) * 5/9
#
# def F(celsius):
#     return 9/5 * celsius +32


#Pitagorov izrek
# def Pitagorov_izrek(a, b):
#     return (a ** 2 + b ** 2)
#
# a = float(input("Vpiši dolžino prve katete pravokotnega trikotnika[mm]:"))
# b = float(input("Vpiši dolžino druge katete pravokotnega trikotnika[mm]:"))
#
# c = a**2 + b**2
# print("Dolžina hipotenuze znaša " f"{c:.3g}mm")

#Topologija
# import math
#
# g = 9.81
# v = float(input("Hitrost izstrelka [m/s]:"))
# fi = float(input("Kot pod katerim je izstrelek izstreljen [stopinje]:"))
# fi_rad = math.pi/180 * fi
#
# s = v ** 2 * math.sin(2*fi_rad)/g
# print("Izstrelek bo izstrelilo " f"{s:.3g} m daleč.")

# Ploščina trikotnika

# a = float(input("Dolžina prve stranice[mm]:"))
# b = float(input("Dolžina druge stranice [mm]:"))
# c = float(input("Dolžina tretje stranice [mm]:"))
#
# s = (a + b + c) / 2
#
# pogoj_1 = s - a
# pogoj_2 = s - b
# pogoj_3 = s - c
# if pogoj_1 < 0 or pogoj_2 < 0 or pogoj_3 < 0:
# print("Dolžina stranic ni ustrezna.")
# else:
# p = (s * (s - a) * (s - b) * (s - c)) ** (1/2)
# print("Ploščina trikotnika znaša " f"{p:.3g} mm^2")


#Poštevanka
#
# import random
#
# a = int(random.randint(2,10))
# b = int(random.randint(2,10))
#
# print("Koliko je " f"{a} krat " f"{b}?")
#
# odgovor = int(input())
# resitev = a * b
#
# if odgovor == a * b:
# print("Bravo, odgovor je pravilen!")
#
# else:
# print("Odgovor je žal napačen, pravilen odgovor je " f"{resitev}.")

#Vsi po 5

# print("Vnesite cene izdelkov:")
# vsota = 0
#
# for x in range(5):
# cena = float(input("Vnesi ceno izdelka:"))
# vsota += cena
#
# print("Vaš račun znaša "f"{vsota} €.")

#Konkurenca

# st_izdelkov = int(input("Vpiši število izdelkov:"))
# vsota = 0
#
# for x in range(st_izdelkov):
# cena_izdelka = float(input("Cena izdelka:"))
# vsota += cena_izdelka
#
# print("Vaš račun znaša " f"{vsota}€. Hvala za obisk.")

# #TopShop
# cena_izdelka = []
# vsota = 0
# while cena_izdelka != 0:
# cena_izdelka = float(input("Vnesite ceno izdelka:"))
# vsota += cena_izdelka
# else:
# print("Vaš račun znaša " f"{vsota}€. Hvala za vaš nakup.")

#DržavnaAgencijaZaVarstvoPotrošnikov

cena_izdelka = 1
vsota = 0
izdelek = 0

while cena_izdelka != 0:
 cena_izdelka = float(input("Vnesite ceno izdelka:"))
 vsota += cena_izdelka
 izdelek += 1
else:
 izdelek -=1
 if izdelek > 0:
 povprecna_cena = vsota/izdelek
 print("Vaš račun znaša " f"{vsota}€. Hvala za vaš nakup.")
 print("Povprečna cena znaša " f"{povprecna_cena}€")