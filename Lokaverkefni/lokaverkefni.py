# Hóp/Lokaverkefni - Ólafur Eysteinn Eysteinsson og Óðinn Kristjánsson - 24. Apríl 2017
import random
stokkur = []
leikmadur1 = []
leikmadur2 = []
jafntefli = []
svar = 1
skra = open("hrutarprufa.txt", "r")
print("Hér eru öll spilin:")
spil = skra.read().split("\n")
skra.close()
# Læt öll spilin í "stokk"
for x in spil:
    stokkur.append(x)
    print(x)
print("")
hve_oft = 1
# Stokka spilin og bý til svo "bunka"random.shuffle(stokkur)
for x in stokkur:
    if hve_oft % 2 == 0:
        leikmadur1.append(x)
        hve_oft = hve_oft + 1
    elif hve_oft % 2 != 0:
        leikmadur2.append(x)
        hve_oft = hve_oft + 1
    else:
        print("Villa!")
random.shuffle(leikmadur1)
random.shuffle(leikmadur2)

while svar == 1:
    for lota in range(1,10000):
        if lota>1:
            svar = input("Næsta lota? *ýttu á Enter* ")
        if len(leikmadur1)==0:
            print("ÞÚ TAPAÐIR!")
            break
        elif len(leikmadur2)==0:
            print("ÞÚ VANNST!")
            break
        print("")
        print("Lota",lota,":")
        for x in leikmadur1:
            flokkar1 = x.split(" ")
            break
        for x in leikmadur2:
            flokkar2 = x.split(" ")
            break
        print("Það eru",len(leikmadur1),"spil í stokknum þínum og",len(leikmadur2),"spil í stokk leikmanns 2.")
        print("Þetta er hrúturinn þinn í þessari lotu:")
        print("Nafn:",flokkar1[0])
        print("1: Þyndgd í kílóum =",flokkar1[1],"kg.")
        print("2: Mjólkuragni dætra =",flokkar1[2])
        print("3: Einkunn ullar =",flokkar1[3])
        print("4: Fjöldi afkvæma =",flokkar1[4])
        print("5: Einkunn læris =",flokkar1[5])
        print("6: Frjosemi =",flokkar1[6])
        print("7: Gerð/Þykkt bakvöðva =",flokkar1[7])
        print("8: Einkunn fyrir malir =",flokkar1[8])
        if lota%2!=0:
            print("Þú velur flokk!")

            val = int(input("Hvaða flokk viltu nota? 1, 2, 3, 4, 5, 6, 7 eða 8 "))
        else:
            print("Leikmaður 2 velur flokk!")
            val=random.randint(1,8)
            print("Leikmaður 2 valdi flokk nr.",val)
        print("")
        if float(flokkar1[val]) > float(flokkar2[val]):
            print("Þú vannst,", flokkar2[0], "fer neðst í stokkinn þinn!")
            print(flokkar1[0], "vann með", flokkar1[val], "á móti", flokkar2[0], "sem var með", flokkar2[val])
            if len(jafntefli) > 0:
                print("Þú fékkst líka", jafntefli)
                for j in range(len(jafntefli)):
                    print(jafntefli[j])
                    leikmadur1.append(jafntefli[j])
                list.clear(jafntefli)
            flokkar1 = " ".join(flokkar1)
            flokkar2 = " ".join(flokkar2)
            leikmadur1.append(flokkar1)
            leikmadur1.append(flokkar2)
        elif float(flokkar1[val]) < float(flokkar2[val]):
            print("Leikmaður 2 vann,", flokkar1[0], "fer neðst í stokkinn hans!")
            print(flokkar2[0], "vann með", flokkar2[val], "á móti", flokkar1[0], "sem var með", flokkar1[val])
            if len(jafntefli) > 0:
                print("Leikmaður 2 fékk líka:")
                for j in range(len(jafntefli)):
                    print(jafntefli[j])
                    leikmadur2.append(jafntefli[j])
                list.clear(jafntefli)
            flokkar1 = " ".join(flokkar1)
            flokkar2 = " ".join(flokkar2)
            leikmadur2.append(flokkar1)
            leikmadur2.append(flokkar2)
        elif float(flokkar1[val]) == float(flokkar2[val]):
            print("Jafntefli!", flokkar1[0], "og", flokkar2[0], "voru með jafnmikið.")
            flokkar1 = " ".join(flokkar1)
            flokkar2 = " ".join(flokkar2)
            jafntefli.append(flokkar1)
            jafntefli.append(flokkar2)
        del leikmadur1[0]
        del leikmadur2[0]
        print("Spilin í pottinum:",jafntefli)