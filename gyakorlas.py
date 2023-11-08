import math
import random


def veletlen():
    i = 0
    while i < 10:
        szam: int = math.floor(random.random() * 21 + 10)
        print(szam, end=" ")
        i += 1


def fel1():
    i = 0
    while i < 5:
        szam: int = math.floor(random.random() * 99 + 1)
        print(szam, end=" ")
        i += 1
    print()

def fel2():
    szam: int = math.floor(random.random() * 90 + 10)
    if szam % 2 == 0:
        print(f"A {szam} páros")
    else:
        print(f"A {szam} páratlan")


def fel3():
    i = 0
    db = 0
    while i < 15:
        szam: int = math.floor(random.random()*2)
        if szam == 1:
            db += 1
        i += 1
    print(f"Ennyi 1-es generált: {db}")


def fel4():
    szam: int = math.floor(random.random()*11 + 1)
    szam2 = szam
    szam2 = szam2 * 3
    szam2 = szam2 - 15
    szam2 = int(szam2/6)
    szam2 = szam2 * 2
    szam2 = szam2 - szam
    if szam2 == 5:
        print("Az eredmény = 5-tel!")
    else:
        print("Az eredmény nem = 5-tel!")


def fel5(szoveg: str):
    print(len(szoveg), end=" ")
    print(szoveg[4].upper())



