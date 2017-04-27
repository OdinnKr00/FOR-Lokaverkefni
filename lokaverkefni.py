#Hóp/Lokaverkefni - Ólafur Eysteinn Eysteinsson og Óðinn Kristjánsson - 24. Apríl 2017
import random

stokkur=[]
leikmadur1=[]
leikmadur2=[]
skra=open("hrutar.txt","r")
print("Hér eru öll spilin:")
spil=skra.read().split("\n")
skra.close()
#Læt öll spilin í "stokk"
for x in spil:
    stokkur.append(x)
    print(x)
print(stokkur)
hve_oft=1
#Stokka spilin og bý til svo "bunka"
random.shuffle(stokkur)
for x in stokkur:
    if hve_oft%2==0:
        leikmadur1.append(x)
        hve_oft=hve_oft+1
    elif hve_oft%2!=0:
        leikmadur2.append(x)
        hve_oft=hve_oft+1
    else:
        print("Villa!")
random.shuffle(leikmadur1)
random.shuffle(leikmadur2)
print(leikmadur1)
print(leikmadur2)
svar=input("Viltu byrja? J fyrir Já")
while svar=="j" or svar=="J":
    for x in leikmadur1:
        flokkar=x.split(" ")
    print(leikmadur1[0])
    print("Viltu nota Þyndgd í kílóum",flokkar[1],", Mjólkuragni dætra",flokkar[2],", Einkunn ullar",flokkar[3],
          ", Fjöldi afkvæma",flokkar[4],", Einkunn læris",flokkar[5],", Frjosemi",flokkar[6],", Gerð/Þykkt bakvöðva",
          flokkar[7],", Einkunn fyrir malir",flokkar[8])
    val=int(input("Hvaða flokk viltu nota? 1, 2, 3, 4, 5, 6, 7 eða 8 "))
    if val==1:
    elif val==2:
    elif val==3:
    elif val==4:
    elif val==5:
    elif val==6:
    elif val==7:
    elif val==8: