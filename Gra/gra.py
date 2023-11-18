import random
import time

pytania=["Jak określa się osobę na pozór spokojną i nieśmiałą?:\nA.ogień i woda B.Słomiany ogień C.Anielska woda D.Cicha woda",
"Umowa cywilnoprawna, zawierana zazwyczaj zamiast umowy o pracę, to tak zwana umowa:\nA.odpadkowa B.śmieciowa C.resztkowa D.okrawkowa",
"Co zalewa ten, kto nie wylewa za kołnierz?:\nA.fundamenty B.ognisko C.zioła D.robaka",
"Co ma na nogach panczenista?:\nA.korki B.narty C.łyżwy D.płetwy",
"Czym bez obaw mozna popić zażywane lekarstwa?:\nA.sokiem z grejfruta B.letnią wodą C.mocną kawą D.gorącą herbatą",
"Jaką cześć liter w wyrazie 'bajzel' stanowią samogłoski?:\nA.jedną piątą B.jedną czwartą C.jedną trzecią D.jedną drugą",
"Litr chłodnej wody waży w przybliżeniu:\nA.10 funtów B.kilogram C.2 dekagramy D.10 uncji",
"Przydomek wiedźmina Geralta wskazuje na to, że bohater sagi Andrzeja Sapkowskiego pochodzi z...\nA.Vengerbergu B.Oxenfurtu C.Rivii D.Tretogoru",
"Ile linii metra jest w Warszawie?\nA.1 B.2 C.3 D.4",
"Pierwsze litery tablicy rejestracyjnej jakiego powiatu tłumaczy się żartobliwie jako Centrum Tadeusza R. albo Co Tu Robisz?\nA.tarnobrzeskiego B.toruńskiego C.tyskiego D.tureckiego",
"Agata Duda witała się ze swoimi uczniami, mówiąc:\nA.Guten Morgen B.Good Morning C.Bonjour D.Boungiorno",
"Które z państw na Bliskim Wschodzie nie graniczy z pozostałymi?\nA.Arabia Saudyjska B.Oman C.Jemen D.Syria",
"Zje pozostałe:\nA.kijanka B.żyworódka rzeczna C.rzęsorek rzeczek D.larwa chruścika",
"Ferruccio Lamborghini, zanim zajął się produkcją samochodów, był producentem przede wszystkim:\nA.motocykli B.tokarek C.ciągników D.maszyn przędzalniczych",
"Dokończ słowa Agnieszki Osieckiej:Do domu wrócimy, w piecu napalimy, nakarmimy psa. Przed nocą zdążymy...\nA.szkopom dołożymy B.tylko zwyciężymy C.wojna to nie gra D.w oku błyśnie łza",
"Robert Pasut, Rafał Masny i Czarek Jóźwik to youtuberzy:\nA.Lekcewarzy B.Abstrachuje C.Ignoróje D.Ómniejsza",
"Płetwą grzbietową nie pruje wody:\nA.Długoszpar B.Kosogon C.Orka D.Wal grenlandzki",
"Który utwór Juliusza Słowackiego napisany jest prozą?\n A.'Godzina myśli' B.'W Szwajcarii' C.'Anheli' D.'Arab'",
"Likier maraskino produkuje się z maraski, czyli odmiany:\nA.wiśni B.jabłoni C.Figi D.Gruszy",
"Który aktor urodził się w roku opatentowania kinematografu braci Lumière?:\nA.Rudolph Valentino B.Humphrey Bogart C.Charlie Chaplin D.Fred Astaire",
"Komiksowym 'dzieckiem' rysownika Boba Kane'a jest:\nA.Superman B.Batman C.Spider-Man D.Captain America",
"Kto jest mistrzem tego samego oręża, w jakim specjalizowała się mitologiczna Artemida?:\nA.Zorro B.Legolas C.Don Kichot D.Longinus Podbipięta",
"Mowa w obronie poety Archiasza przeszła do historii jako jeden z najświetniejszych popisów retorycznych:\nA.Izokratesa B.Cycerona C.Demostenesa D.Kwintyliana",
"Rybą nie jest:\nA.Świnka B.Rozpiór C.Krasnopiórka D.Kraska",
"Odrażający drab z Kabaretu Starszych Panów dubeltówkę weźmie, wyjdzie i...\nA.Rach-ciach! B.Buch,Buch! C.Z rur dwóch D.Bum w brzuch",
"Kto był nadwornym malarzem króla Filipa IV Habsburga?:\nA.Marcello Bociarelli B.Jan van Eyck C. Diego Velazquez D.Jaques-Louis David",
"Z gry na jakim instrumencie słynie Czesław Mozil?:z\nA.Na kornecie B.Na akordeonie C.Na djembe D.Na ksylofonie"]

odpowiedzi=["D","B","D","C","B","C","B","C","B","B","A","D","C","C","B","B","D","C","A","A","B","B","D","D","B","C","D"]

komentarz_pytanie = ["Czy to jest Twoja ostateczna odpowiedź?",
"Czy jesteś pewnien swojej odpowiedzi?",
"Jesteś pewien, że nie chcesz zmienić odpowiedzi?",
"Definitywnie?",
"Czy to jest twoja ostateczna decyzja?",
"Obstajesz przy swoim?",
"Czy Twoja mama poparłaby Twój wybór?",
"Zastanowiłeś się dobrze?",
"Rozumiem, że nie zmienisz już zdania?",
"Czy to jest na 100% dobra odpowiedź?",
"Widzę, że się nie wahasz. Mam rację?",
"Na pewno ta odpowiedź?"]

kwoty = ["500 zł","1 000 zł", "2 000 zł", "5 000 zł", "10 000 zł", "20 000 zł", "40 000 zł", "75 000 zł", "125 000 zł", "250 000 zł", "500 000 zł", "1 000 000 zł"]

mozliwe_odp = ["A","B","C","D"]
odp_wagi1 = [0.85,0.05,0.05,0.05]
odp_wagi2 = [0.7,0.1,0.1,0.1]
odp_wagi3 = [0.55,0.15,0.15,0.15]

kola_ratunkowe = ["Telefon do przyjaciela", "Pół na pół", "Pytanie do publiczności"]

licznik = 0
odpowiedz2=0
print("Witam, nazywam się Hubert Urbański i będę prowadził Twoją dzisiejszą grę. \nPowiedz jak się nazywasz uczestniku!")
uczestnik = input()

numer_pytania = []
for b in range(12):
    r = random.randint(1,26)
    if r not in numer_pytania:
        numer_pytania.append(r)
while True:
        time.sleep(2)
        kola_ratunkowe1=kola_ratunkowe
        print("Masz dostęp do kół ratunkowych:\n" ,"1. ", kola_ratunkowe1[0], "\n2. ", kola_ratunkowe1[1], "\n3. ", kola_ratunkowe1[2],"\n")
        time.sleep(3)
        i = numer_pytania[licznik]
        print("Pytanie:",pytania[i])
        mozliwe_odp = ["A","B","C","D"]
        kolo = str(input("Czy chcesz wykorzystać koło ratunkowe?\n"))
        if kolo == "tak":
            x=0
            while x<1:
                print("Które koło chcesz wykorzystać?")
                kolo_wybor = int(input())
                if kola_ratunkowe1[kolo_wybor - 1]=="X":
                    print("To koło zostało już wybrane")
                else:
                    x=+1
            if kolo_wybor == 1:
                print("Wybrałeś: ", kola_ratunkowe[0])
                print("Dzwonimy do Twojej mamy bo nie masz przyjaciół")
                print("Dzień dobry pani mamo, jaka według pani będzie prawidłowa odpowiedź?")
                p2 = mozliwe_odp
                for n in p2[:]:
                    if n == odpowiedzi[i]:
                        p2.remove(n)
                p3 = [odpowiedzi[i],p2[0],p2[1],p2[2]]
                if licznik <= 5:
                    podpowiedz = random.choices(p3,odp_wagi1)
                elif licznik > 5 and licznik <= 9:
                    podpowiedz = random.choices(p3,odp_wagi2)
                elif licznik > 9 and licznik <= 12:
                    podpowiedz = random.choices(p3,odp_wagi3)
                time.sleep(3)
                print("MAMA: Według mnie odpowiedzią na to pytanie będzie: ", podpowiedz, "\nA na obiad będą ziemniaki\n")
                kola_ratunkowe1[0]="X"
            elif kolo_wybor == 2:
                print("Wybrałeś: ", kola_ratunkowe[1])
                print("Proszę o usunięcie połowy odpowiedzi")
                p2 = mozliwe_odp
                for n in p2[:]:
                    if n == odpowiedzi[i]:
                        p2.remove(n)
                podpowiedz2 = random.choice(p2)
                time.sleep(2)
                print("Pozostawione odpowiedzi: ", odpowiedzi[i],"oraz", podpowiedz2)
                kola_ratunkowe1[1]="X"
            elif kolo_wybor == 3:
                print("Wybrałeś: ", kola_ratunkowe[2])
                print("Jaka odpowiedż jest prawidłowa według publiczności?")
                p2 = mozliwe_odp
                for n in p2[:]:
                    if n == odpowiedzi[i]:
                        p2.remove(n)
                p3 = [odpowiedzi[i],p2[0],p2[1],p2[2]]
                if licznik <= 5:
                    podpowiedz = random.choices(p3,odp_wagi1)
                elif licznik > 5 and licznik <= 9:
                    podpowiedz = random.choices(p3,odp_wagi2)
                elif licznik > 9 and licznik <= 12:
                    podpowiedz = random.choices(p3,odp_wagi3)
                time.sleep(4)
                print("Publiczność zadecydowała! Według nich odpowiedzią będzie:  ", podpowiedz)
                kola_ratunkowe1[2]="X"
        else:
            print("No to jesteś zdany na samego siebie")

        print("Jaka jest Twoja odpowiedź?")
        odpowiedz=input()
        while True:
            j = random.randint(0,11)
            print(komentarz_pytanie[j])
            odp1 = input()
            if odp1 == "tak" or odp1 == "Tak":
                print("W takim razie zaznaczam odpowiedź ", odpowiedz)
                break
            elif odp1 == "nie" or odp1 == "Nie":
                print(uczestnik, ", czy w takim razie chcesz zmienić swoją odpowiedź?")
                odp2 = input()
                if odp2 == "tak" or odp2 == "Tak":
                    print("Na którą opcję zmieniasz?")
                    odpowiedz2 = input()
                    odpowiedz = odpowiedz2
                elif odp2 == "nie" or odp2 == "Nie":
                    print("Skoro tak mówisz, zaznaczam odpowiedź ", odpowiedz)
                else:
                    print(uczestnik,",konkretnie proszę - tak czy nie?")
            else:
                print(uczestnik, ", nie ma, że \"",odp1, "\" potrzebuję definitywnej odpowiedzi - tak lub nie!")
        if odpowiedz==odpowiedzi[i]:
            licznik = licznik + 1
            l=licznik-1
            time.sleep(3)
            print("\nTo jest poprawna odpowiedź.\n Zdobywasz " , kwoty[l], "\n")
            if licznik == 2 or licznik == 7:
                print("To kwota gwarantowana\n")
            if licznik == 12:
                print("\nTAK, TO JEST POPRAWNA ODPOWIEDŹ! WYGRYWASZ 1 000 000 ZŁOTYCH!")
                break
        else:
            time.sleep(3)
            print("\nTo zła odpowiedź\n Dla Ciebie ",uczestnik," nasza przygoda po milion się kończy!")
            if licznik >= 2 and licznik < 7:
                print("Otrzymujesz kwotę gwarantowaną 1 000 zł!")
            elif licznik >= 7:
                print("Otrzymujesz kwotę gwarantowaną 40 000 zł!")
            break



if odpowiedz[-1] == odpowiedzi[i]:
    print("TAK, TO JEST POPRAWNA ODPOWIEDŹ! WYGRYWASZ 1 000 000 ZŁOTYCH!")