# 1. feladat
# Olvassa be és tárolja el a melyseg.txt állomány adatait, és annak felhasználásával oldja
# meg a következő feladatokat! 

melysegek=[]
with open("./melyseg.txt","r",encoding="utf-8") as fm1:
    fm1.readline()
    fm1.readline()
    for sor in fm1:
        seged_lista=list(map(int,sor.strip().split()))
        #print(seged_lista)
        melysegek.append(seged_lista)

#print(melysegek)

from colorama import Fore, Back

for melyseg_sor in melysegek:
    for melyseg in melyseg_sor:
        if melyseg>0:
            print(f"{Back.BLUE}{Fore.RED}{melyseg:2d}", end=" ",)
        else:
            print(f"{Back.RESET}{Fore.BLACK}{melyseg:2d}", end=" ",)
    print()

# tört x=3.1415     print(f"{x:0.2f}")
# egész y=1         print(f"{y:2d}"")

print("2. feladat")
be_sor=int(input("A mérés sorának azonosítója= ") or "12") 
be_oszlop=int(input("A mérés sorának azonosítója") or "6") 

print(f"A mért mélység az adott helyen {melysegek[be_sor-1][be_oszlop-1]} dm")

print("3.feladat")

def megszamolas(m):
    darab=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                darab+=1
    return darab

felszin=megszamolas(melysegek)

def atlagolas(m):
    osszeg=0
    darab=0
    for seged_lista in m:
        for elem in seged_lista:
            if elem>0:
                darab+=1
                osszeg+=elem
    return osszeg/darab

print(f"A tó felszíne: {felszin} m2, átlagos mélysége: {atlagolas(melysegek)/10:0.2f} m")

print("4. feladat")

def max_kivalasztas(m):
    max_sor=0
    max_oszlop=0
    for i in range(1,len(m)):
        for j in range(len(m[i])):
            if m[max_sor][max_oszlop]<m[i][j]:
                max_sor=i
                max_oszlop=j
    return max_sor, max_oszlop

max_s, max_o=max_kivalasztas(melysegek)

print(f"A tó legnagyobb mélysége: {melysegek[max_s][max_o]} dm")


print(f"A legmélyebb helyek sor-oszlop koordinátái:")
def legmelyebb_pontok_koordinatai(m, max):
    for sor_index, sor in enumerate(m):
        for elem_index, elem in enumerate(sor):
            if elem==max:
                print(f"({sor_index+1}; {elem_index+1}) ", end="")


legmelyebb_pontok_koordinatai(melysegek, melysegek[max_s][max_o])



