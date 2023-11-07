import math
from builtins import str


def fel1():
    print("feladat:1.Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van,"
          "jelezz hibát!), majd írasd ki az első számjegyét!")
    szam: int = int(input("Adjon meg egy számot 200-920 közöt!"))
    while not szam > 200 and szam < 920:
        print("Hiba: nem az intervalumba van!")
        szam: int = int(input("Adjon meg egy számot 200-920 közöt!"))
    elsoSz = int(str(szam)[0])
    print(elsoSz)


def fel2(szam):
    print("feladat:2.	Írj metódust, mely a paraméterében kapott számról megmondja, hogy hány 1-es, 10-es, 100 - as, 1000 - es, stb van benne! használd hozzá az egész osztás operátorát - // ! pl: 123//10 =12  123%10=3")
    ezresek = szam // 1000
    szazas = szam // 100
    tizes = szam // 10
    egyesek = szam // 1
    print(f"ezresek:{ezresek:.0f}\nszázasok:{szazas:.0f}\ntízedesek:{tizes:.0f}\negyesek:{egyesek:.0f}")


def fel3():
    print("feladat:3.	+++ Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre. PL. 324 -> „324 számjegyeinek összege: 9")
    szam = input("Adjon meg egy számot!")
    i = 0
    osszeg = 0
    while i < len(szam):
       osszeg += int(str(szam)[i])
       i += 1
    print(f"{szam},számjegyeinek összege:{osszeg}")


def fel4():
    print("feladat:4.	Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani. "
          "A 2-3. órában már kissé éhesek, és csupán 60%-os a munkabírásuk. "
          "A 4-7. órában szerencsére programozást tanulnak, így némiképp javul a hatékonyságuk (70%), a 8-9. "
          "órában azonban már újra lecsökken (50%)."
          "Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát, ha nem ebben az intervallumban lévő számot kapsz,"
          " pl. “Ez már tényleg túlzás.”). Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”    -  nem kell tesztfüggvényeket írni, de az alábbi táblázat alapján ellenőrizzétek a munkátokat!")
    szam: int = int(input("Adjon meg 1-9-ig egy számot!"))
    if szam == 1:
        print("Még 90% on vagyunk!")
    elif szam == 2 or szam == 3:
        print("Még bírjuk (60%)")
    elif szam == 4 or szam == 5 or szam == 6 or szam == 7:
        print("Progit tanulunk, töltődünk! 70%")
    elif szam == 8 or szam == 9:
        print("Lassan nem bírjuk tovább! 50%")
    elif szam == 10 or szam > 10:
        print("Ez már tényleg túlzás.")
    elif szam == 0:
        print("Be se jövök!")
    else:
        print("Hiba!")


def fel5():
    print("feladat:5.	Az egyik diák (legyen Márti a neve) az alábbi algoritmus alapján tevékenykedik az órákon:"
          "a.	hétfőn alszik az összes órán,"
          "b.	kedden csak hittan órán figyel,"
          "c.	programozás órán dolgozik, de csak szerdánd."
          "d.	csütörtökön minden órán figyel, mert jó kedve van (aznap szokott moziba menni)"
          ",e.	pénteken a hétvégéről ábrándozik, így csak félig figyel minden aznapi órán,"
          "f.	a többi óráról semmit nem tudunk."
          "Írj metódsut, melynek  2 bemenő prarmétere van (nap neve, óra neve) és tájékoztatást ad Márti állapotáról. ")
    nap: str = input("Adja meg a napot!")
    ora: str = input("Adja meg az órát!")
    if nap == "hétfő":
        print(f"{nap}; {ora}; alszik")
    elif nap == "kedd" and ora == "hittan":
        print(f"{nap}; {ora}; figyel")
    elif nap == "kedd" and ora != "hittan":
        print(f"{nap}; {ora}; alszik")
    elif nap == "szerda" and ora == "programozás":
        print(f"{nap}; {ora}; dolgozik")
    elif nap == "szerda" and ora != "programozás":
        print(f"{nap}; {ora}; nincs info")
    elif nap == "csütörtök":
        print(f"{nap}; {ora}; figyel")
    elif nap == "péntek":
        print(f"{nap}; {ora}; félig van jelen")
    else:
        print("Hibás adatot adtál meg!")


def fel6():
    print("feladat:6.	A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, "
          "ha a felhasználó negatív számból akar gyököt vonni!")
    szam: float = float(input("Adjon meg egy számot!"))
    if szam < 0:
        print("Hiba: A szám nem lehet negatív!")
        return
    gyok = math.sqrt(szam)
    print(f"Meg adott szám:{szam}, Gyöke: {gyok}")


def fel7():
    print("feladat:7.	A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, "
          "akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, "
          "területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "
          "Hiba: a téglalap oldalai nem pozitívak!!")
    szam1: float = float(input("Adjon meg egy számot!"))
    szam2: float = float(input("Adjon meg  még egy számot!"))
    while szam1 < 0 or szam2 < 0:
        print("Hiba: a téglalap oldalai nem pozitívak!")
        szam1: float = float(input("Adjon meg egy számot!"))
        szam2: float = float(input("Adjon meg  még egy számot!"))
    kerulet = (szam1 + szam2)*2
    terulet = szam1 * szam2
    print(f"Kerület: {kerulet:.2f} Terület: {terulet:.2f} A oldal: {szam1} B oldal: {szam2}")


def kiallitasfel():
    print("feladat:1.feladat:	Egy a természettel  Vadászati és Természeti Világkiállításon téged bíztak meg, "
          "hogy egy kihelyezett információs tábla részműködését leprogramozd!"
          "A felhasználónak be kell gépelnie melyik szektort szeretné megnézni,"
          " a te programod pedig kiírja az ott található kiállítás nevét."
          "•A esetén Nemzetközi Csarnok, World Conservation Forum 2021"
          "•B és E esetén a Kereskedelmi Csarnok felirat jelenjen meg"
          "•C esetén Konferencia-központ Innovációs Showroom"
          "•D esetén Hal, Víz és Ember"
          "•F esetén Hagyományos Vadászati Módok Csarnoka"
          "•G Hazai és nemzetközi Trófeakiállítás, 12. Nyílt Európai Taxiderma-bajnokság, Vadászat 21.században kiállítás"
          "•H esetben Központi Magyar Kiállítás"
          "•Minden egyéb nem szám adatra írja ki, hogy forduljon a pénztárhoz.")
    sector: str = input("Adjon meg egy szektort!")
    if sector == "A" or sector == "a":
        print("Nemzetközi Csarnok, World Conservation Forum 2021")
    elif sector == "B" or sector == "E" or sector == "b" or sector == "e":
        print("Kereskedelmi Csarnok")
    elif sector == "C" or sector == "c":
        print("Konferencia-központ Innovációs Showroom")
    elif sector == "D" or sector == "d":
        print("Hal, Víz és Ember")
    elif sector == "F" or sector == "f":
        print("Hagyományos Vadászati Módok Csarnoka")
    elif sector == "G" or sector == "g":
        print("Hazai és nemzetközi Trófeakiállítás,\n "
              "12. Nyílt Európai Taxiderma-bajnokság,\n "
              "Vadászat 21.században kiállítás")
    elif sector == "H" or sector == "h":
        print("Központi Magyar Kiállítás")
    else:
        print("HIBA: Adjon meg egy betűt A-H-ig!")


def fel8():
    print("feladat:8.Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! "
          "10-esével egymás alá! használj hozzá formázott kiiratást!")
    for x in range(1, 11):
        for y in range(1, 11):
            print('{:3}'.format(x * y), end=' ')
        print()


def fel9():
    print("feladat:9.Írj metódust, mely neveket kér a felhasználótól addig amíg a „@” jelet nem kapja."
          " Hány nevet adott meg a felhasználó? "
          "Van-e benne A betűvel kezdődő név? "
          "Melyik a leghosszabb név? ")
    db: int = 0
    leghosszabb = ""
    nev: str = input("Adjon egy nevet! ('@'írjon,hogy befejezze)")
    while nev != "@":
        db += 1
        if len(nev) > len(leghosszabb):
            leghosszabb = nev
        hely = nev.find("A")
        if hely == 0:
            vanA: str = "Igen volt"
        else:
            vanA: str = "Nem volt"
        nev: str = input("Adjon egy nevet! ('@'írjon,hogy befejezze)")

    print(f"Meg adott nevek száma: {db}\nVolt-e A betűvel kezdődő név? {vanA}\nA leghosszabb név: {leghosszabb}")


def fel10():
    print("feladat:10.	Írj metódust, mely egy érmedobás eredményét kéri be a felhasználótól 10-szer egymás után!"
          " A felhasználó minden lépésben a „f” vagy  „i” betűket kell megadjon. "
          "Addig kérd be a jeleket, amíg jó jelet nem ad meg. "
          "Hányszor adott meg „f” betűt?"
          "Mekkora a leghosszabb f sorozat?")
    eredmeny: str = input("Adja meg az eredményt!(f,i)")
    db = 0
    hasonlo = 0
    i = 1
    while i < 10:
        while not (eredmeny != "f" or eredmeny != "i"):
            print("nem jó!")
            eredmeny: str = input("Adja meg az eredményt!(f,i)")
        if eredmeny == "f":
            db += 1
        if eredmeny[i] == "f" and eredmeny[i] == "f":
           hasonlo += 1
        i += 1
    print(f"")


def fel11():
    print("feladat:11.	++ Írj programot, mely beolvas egy pozitív egész számot, és megmondja, hogy tökéletes szám-e! "
          "(A tökéletes számok azok, melyek osztóinak összege egyenlő a szám kétszeresével."
          " Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.) ")
    szam: int = int(input("Adjon egy számot!"))
    osztokosszege = 0
    for i in range(1, szam + 1):
        if szam % i == 0:
            osztokosszege += i
    if szam * 2 == osztokosszege:
        print(f"{szam} egy tökéletes szám!")
    else:
        print(f"{szam} nem tökéletes szám!")








