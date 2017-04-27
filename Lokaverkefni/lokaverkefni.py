# Hóp/Lokaverkefni - Ólafur Eysteinn Eysteinsson og Óðinn Kristjánsson - 24. Apríl 2017
import random
import time
stokkur = []
leikmadur1 = []
leikmadur2 = []
skra = open("hrutar.txt", "r")
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
svar = input("Viltu byrja? J fyrir Já ")

while svar == "j" or svar == "J":
    for lota in range(1,10000):
        print("")
        print("Lota",lota,":")
        for x in leikmadur1:
            flokkar1 = x.split(" ")
            break
        for x in leikmadur2:
            flokkar2 = x.split(" ")
            break
        #for i in flokkar2:
           # if i.isdigit() == True or i.replace(".", "", 1).isdigit() == True:
               # print(i)
        print("Það eru",len(leikmadur1),"spil í stokknum þínum og",len(leikmadur2),"spil í stokk leikmanns 2.")
        print("Þetta er hrúturinn þinn í þessari lotu:",flokkar1)
        if lota%2!=0:
            print("Þú velur flokk!")
            print("Viltu nota Þyndgd í kílóum, Mjólkuragni dætra, Einkunn ullar, Fjöldi afkvæma"
                  ", Einkunn læris, Frjosemi, Gerð/Þykkt bakvöðva eða Einkunn fyrir malir")
            val = int(input("Hvaða flokk viltu nota? 1, 2, 3, 4, 5, 6, 7 eða 8 "))
        else:
            print("Talvan velur flokk!")
            val=random.randint(1,8)
            print("Talvan valdi flokk nr.",val)
        if val == 1:
            if float(flokkar1[1]) > float(flokkar2[1]):
                print(flokkar1[0],"vann með",flokkar1[1],"á móti",flokkar2[0],"sem var með",flokkar2[1])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[1]) < float(flokkar2[1]):
                print(flokkar2[0],"vann með",flokkar2[1],"á móti",flokkar1[0],"sem var með",flokkar1[1])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[1]) > float(flokkar2[1]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]
        elif val == 2:
            if float(flokkar1[2]) > float(flokkar2[2]):
                print(flokkar1[0],"vann með",flokkar1[2],"á móti",flokkar2[0],"sem var með",flokkar2[2])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[2]) < float(flokkar2[2]):
                print(flokkar2[0],"vann með",flokkar2[2],"á móti",flokkar1[0],"sem var með",flokkar1[2])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[2]) > float(flokkar2[2]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]
        elif val == 3:
            if float(flokkar1[3]) > float(flokkar2[3]):
                print(flokkar1[0],"vann með",flokkar1[3],"á móti",flokkar2[0],"sem var með",flokkar2[3])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[2]) < float(flokkar2[3]):
                print(flokkar1[0],"vann með",flokkar1[3],"á móti",flokkar2[0],"sem var með",flokkar2[3])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[3]) > float(flokkar2[3]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]
        elif val == 4:
            if float(flokkar1[4]) > float(flokkar2[4]):
                print(flokkar1[0],"vann með",flokkar1[4],"á móti",flokkar2[0],"sem var með",flokkar2[4])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[4]) < float(flokkar2[4]):
                print(flokkar1[0],"vann með",flokkar1[4],"á móti",flokkar2[0],"sem var með",flokkar2[4])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[4]) > float(flokkar2[4]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]
        elif val == 5:
            if float(flokkar1[5]) > float(flokkar2[5]):
                print(flokkar1[0],"vann með",flokkar1[5],"á móti",flokkar2[0],"sem var með",flokkar2[5])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[5]) < float(flokkar2[5]):
                print(flokkar1[0],"vann með",flokkar1[5],"á móti",flokkar2[0],"sem var með",flokkar2[5])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[5]) > float(flokkar2[5]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]
        elif val == 6:
            if float(flokkar1[6]) > float(flokkar2[6]):
                print(flokkar1[0],"vann með",flokkar1[6],"á móti",flokkar2[0],"sem var með",flokkar2[6])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[6]) < float(flokkar2[6]):
                print(flokkar1[0],"vann með",flokkar1[6],"á móti",flokkar2[0],"sem var með",flokkar2[6])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[6]) > float(flokkar2[6]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]
        elif val == 7:
            if float(flokkar1[7]) > float(flokkar2[7]):
                print(flokkar1[0],"vann með",flokkar1[7],"á móti",flokkar2[0],"sem var með",flokkar2[7])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[7]) < float(flokkar2[7]):
                print(flokkar1[0],"vann með",flokkar1[7],"á móti",flokkar2[0],"sem var með",flokkar2[7])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[7]) > float(flokkar2[7]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]
        elif val == 8:
            if float(flokkar1[8]) > float(flokkar2[8]):
                print(flokkar1[0],"vann með",flokkar1[8],"á móti",flokkar2[0],"sem var með",flokkar2[8])
                print("Þú vannst,",flokkar2[0],"fer neðst í stokkinn þinn!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur1.append(flokkar1)
                leikmadur1.append(flokkar2)
            elif float(flokkar1[8]) < float(flokkar2[8]):
                print(flokkar1[0],"vann með",flokkar1[8],"á móti",flokkar2[0],"sem var með",flokkar2[8])
                print("Talvan vann,", flokkar1[0], "fer neðst í stokkinn hans!")
                flokkar1=" ".join(flokkar1)
                flokkar2=" ".join(flokkar2)
                leikmadur2.append(flokkar1)
                leikmadur2.append(flokkar2)
            elif float(flokkar1[8]) > float(flokkar2[8]):
                print("Jafntefli")
            del leikmadur1[0]
            del leikmadur2[0]