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

# cena_izdelka = 1
# vsota = 0
# izdelek = 0
#
# while cena_izdelka != 0:
#  cena_izdelka = float(input("Vnesite ceno izdelka:"))
#  vsota += cena_izdelka
#  izdelek += 1
# else:
#  izdelek -=1
#  if izdelek > 0:
#  povprecna_cena = vsota/izdelek
#  print("Vaš račun znaša " f"{vsota}€. Hvala za vaš nakup.")
#  print("Povprečna cena znaša " f"{povprecna_cena}€")

#10 Collatzova domneva
#
# a = int(input("Vpiši celo število: "))
#
# while True:
#  print(a)
#  if a == 1:
#      break
#  if (a % 2) == 0:
#   a = a/2
#  else:
#   a = a * 3 + 1


#11 Benjnaminovi konvanci

# import random
#
# def vrzi():
#  return random.choice("CG")
#
# st_kovancev = 5
#
# while 0 < st_kovancev < 10:
#    met = vrzi()
#    if met == "G":
#       st_kovancev += 1
#    else:
#       st_kovancev -= 1
#    print(met,st_kovancev)

#12 Tekmovanje iz poštevanke
# tocka1 = tocka2 = 0
#
# while abs(tocka1 - tocka2) < 2:
#    a = int(input("Tekmovalec 1, prvi faktor: "))
#    b = int(input("Tekmovalec 1, drugi faktor: "))
#    rez2 = int(input("Tekmovalec 2, produkt:"))
#
#    if a * b == rez2:
#       tocka2 += 1
#
#    a = int(input("Tekmovalec 2, prvi faktor: "))
#    b = int(input("Tekmovalec 2, drugi faktor: "))
#    rez1 = int(input("Tekmovalec 1, produkt"))
#
#    if a * b == rez1:
#       tocka1 += 1
#
#    print(f"Rezultat je {tocka1} : {tocka2}")
#
# else:
#    print(f"Tekma je končana. Končni rezultat je {tocka1} : {tocka2}")
#
# if tocka1 > tocka2:
#    print("Bravo prvi, drugi cvek!")
# else:
#    print("Bravo drugi, prvi cvek!")

#16 Vsota elementov seznama
#
# s = [5, 8, 3, 6, 0, 1]
# def vsota(s):
#    return sum(s)
#
# vsota = sum(s)
# print(vsota)

#17 Ajavost nizov
#
# besedilo ="Danes je lep sončen dan. Sky leži v svojem pesjaku in se nastavlja sončnim žarkom. Kmalu bova šla na sprehod."
# s = besedilo.count("a")
# print(f"Število a-jev je:{s}")

#39Index telesne mase

# podatki = [
#    ["Ana", 55, 165],
#    ["Berta", 60, 153]
# ]
# for ime, teza, visina in podatki:
#    print(ime, teza/ (visina/100) ** 2)

#Seznam trojk
# seznam = [(3, 5, 8), (9, 3, 6), (1, 2, 1), (10, 5, 15)]
#
# def trojke(seznam):
#    for x, y, z in seznam:
#       if x + y != z:
#          return False
#    return True
#
# print(trojke(seznam))
#
# def trojke_splosno(seznam):
#    for x,y,z in seznam:
#       if x + y !=z and x + z !=y and y + z != x:
#          return False
#    return True
#
# print(trojke_splosno(seznam))

#41 Skalarni produkt

# u = [1, 2, 3]
# v = [5, 4, 6]
# def skalarni(u,v):
#     vsota = 0
#     for x,y in zip(u,v):
#         vsota += x * y
#     return vsota
#
# print(skalarni(u,v))

#42 Ujemanja črk
# a = "pav"
# b = "krvavica"
#
# def st_ujemanj(a, b):
#     count = 0
#     for x, y in zip(a, b):
#         if x == y:
#             count += 1
#         else:
#             count = count
#     return count
#
# print(st_ujemanj(a, b))

#47Olimpijske medalje

# def napredek(p):
#     count_napr = 0
#     count_naz =0
#     for x, y in enumerate(p, 1):
#         if x > y:
#             count_napr += 1
#         elif x < y:
#             count_naz += 1
#         else:
#             None
#     return count_naz, count_napr
#
# p = [1, 3, 2, 4, 6, 10, 7, 5, 9, 8]
# print(napredek(p))

#48 Vstavi teže
# def vstavi_teze(osebe, teze):
#     i = 0
#     for j, ime in enumerate(osebe):
#         if ime[-1] != "a":
#             osebe[j] = teze[i]
#             i += 1
#     return osebe
#
#
# osebe = ["Adam", "Eva", "Kajn", "Abel"]
# teze = [87, 86, 75]
# print(vstavi_teze(osebe, teze))

#49 Primerjanje seznamov

def primerjaj(s,t):
    #for s in t:
        #return 0
    for i,j in zip(s,t):
        if s[i] == t[j]:
            p == 0



s = [1, 2, 3]
t = [1, 8, 2]
print(primerjaj(s, t))