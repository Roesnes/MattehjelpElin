Følgende data for USAs befolkning er gitt: 

USAbefolkning.csv
```csv
År;Populasjon
1790;3.929
1800;5.308
1810;7.240
1820;9.638
1830;12.866
1840;17.069
1850;23.192
1860;31.443
1870;38.558
1880;50.156
1890;62.948
1900;75.996
1910;91.972
1920;105.711
1930;122.775
1940;131.669
1950;150.697
1960;179.323
1970;203.185
1980;226.546
1990;248.710

```
Vi vil lage ei .csv-fil med disse dataene. Det gjøres enkelt ved å lime dataene inn i 'notisblokk' eller tilsvarende applikasjon (jeg bruker Notepad++), for så å lagre filen med et navn etterfulgt av endingen .csv som definerer formatet. Det kan også gjøres direkte i Spyder ved å lage ei ny fil, gi den navn, for så å sørge for at navnet ender med .csv. 


Det er gitt et kodeeksempel for plotting av kaffetemperatur: 

Kopier denne koden og lagre den i Spyder som en fil i .py-format. 
KaffePlot.py med kommentarer for hva hver linje i programmet gjør: 
```Python
import pandas as pd # Importer pandas-biblioteket og gir det forkortelsen 'pd'. 
import numpy as np # Importer numpy-biblioteket og gir det forkortelsen 'np'. 
import matplotlib.pyplot as plt # Importer modulen 'pyplot' fra matplotlib-biblioteket og gir den forkortelsen 'plt'. 

df = pd.read_csv('kaffetemperatur.csv', sep=';', comment='#', decimal=',')
# Her definerer vi 'df' (dataframe) til å være innholdet i 'kaffetemperatur.csv'. 
# sep=';' bestemmer at kolonner er separert med semikolon. 
# comment='#' ignorerer linjer som starter med #. (det øverste i din fil, jeg gadd ikke å kopiere det med her hehe)
# decimal=',' tolker komma ',' som desimalskille. 

tid = df['Tid'].tolist()
# Henter kolonnen "Tid" fra 'df' (dataframe) og gjør den om til en vanlig liste i Python. 
temperatur = df['Temperatur'].tolist()
# Henter kolonnen "Temperatur" og gjør den om til en vanlig liste i Python. 

plt.figure(figsize=(12, 5))
# Lager en ny figur med bredde 12 og høyde 5. 
plt.scatter(tid, temperatur, color='r')
# Tegner et scatter plot av tid mot temperatur, med røde punkter. 
#plt.plot(tid, temperatur) <-- Denne linjen var allerede kommentert ut, men ved fjerning av '#' i starten av linjen, så ville det blitt tegnet en sammenhengende linje gjennom punktene. 

plt.title("Temperatur i kaffekopp") # Setter tittel på grafen. 
plt.xlabel("Tid/minutter") # Setter tekst på x-aksen. 
plt.ylabel("Temperatur i grader") # Setter tekst på y-aksen. 
plt.grid() # Aktiverer rutenett i bakgrunnen (for å gjøre det enklere å lese verdier)
plt.show() # Viser figuren i et vindu. 

```
Denne kan vi bruke videre med noen få justeringer. Endringene jeg vil gjøre, er som følger: 
1. Endre programmet til å lese .csv-filen jeg har laget. 
2. Endre kolonnene som skal hentes til å tilsvare kolonnene i .csv-filen ``År;Populasjon``
3. Lag plottet med nye titler for plot og akser. 

Slik ser koden ut etter tilpasning etter data i .csv-filen vi lagde: 
USAbefolkning.py
```Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leser inn min fil
df = pd.read_csv("USAbefolkning.csv", sep=";", comment="#", decimal=".")
# Her har jeg endret til rikitg filnavn og beholdt resten. Vær obs på at hvis du har et datasett som er separert av et annet symbol enn ';' eller bruker vanlig komma som desimal, så må dette endres. Vi trenger ikke det i dette tilfellet. 

# Hent kolonnene som lister
ar = df["År"].tolist()
befolkning = df["Populasjon"].tolist()
# Her har jeg bare endret navnet på listene vi lager. I eksempelet bruker de "Tid" og "Temperatur", men i vårt tilfelle passer det bedre å endre til noe annet som representerer vårt datasett. 

# Lag plottet
plt.figure(figsize=(12, 5))
plt.scatter(ar, befolkning, color="r") # Endret for å tilsvare datasettet. 
plt.plot(ar, befolkning) # Fjernet '#' og hentet listene vi definerte lengre oppe. Nå vil det tegnes en linje mellom punktene. 
plt.title("Befolkning i USA") # Endret til en passende tittel. 
plt.xlabel("År") # Endret til paassende navn på x-aksen. 
plt.ylabel("Befolkning (millioner)") # Endret til passende navn på y-aksen. 
plt.grid()
plt.show()
# Her må man være obs på at navnet på listene vi henter, matcher listene vi lagde lengre oppe. 

```

Når denne filen kjøres, plottes punktene og det trekkes en rød linje punkt-for-punkt. 

Vi vil nå legge til deler i programmet. Vi må: 
- Plotte punktene (allerede gjort). 
- Finne et polynom $f$ med regresjon. 
- Tegne $f(x)$. 
- Tegne $f'(x)$ og $f''(x)$.  
- Finne et stasjonært punkt ved hjelp av en while-løkke. 

Jeg endrer programmet: 
```Python
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 01:42:46 2025

@author: marcu
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1) Les inn filen
df = pd.read_csv("USAbefolkning.csv", sep=";", comment="#", decimal=".")

# 2) Hent kolonnene som lister
ar = df["Ar"].tolist()
befolkning = df["Populasjon"].tolist()

# Gjør om til NumPy-arrays (nyttig for videre beregning)
x = np.array(ar)
y = np.array(befolkning)

# 3) Plott de opprinnelige datapunktene
plt.figure(figsize=(12, 5))
plt.scatter(x, y, color="r", label="Data")
plt.plot(x, y, color="k", linestyle="--", label="Linje mellom punkter")
plt.title("Befolkning i USA")
plt.xlabel("År")
plt.ylabel("Befolkning (millioner)")
plt.grid()
plt.legend()
plt.show()

# 4) Finn et polynom f(x) som passer dataene (regresjon)
grad = 3                       # Jeg velger graden på polynomet (her 3. grad)
koeff = np.polyfit(x, y, grad) # Jeg beregner koeffisientene til et 3.-gradspolynom som best tilpasser dataene. 
f = np.poly1d(koeff)           # Lager et polynom-objekt f(x) basert på koeffisientene. 

print("Polynom f(x):")         # Skriver en overskrift i konsollen. 
print(f)                       # Skriver ut funksjonsuttrykket i konsollen. 

# 5) Lag glatte x-verdier og beregn f(x), f'(x), f''(x)
x_glatt = np.linspace(min(x), max(x), 500) # Lager 500 jevnt fordelte x-verdier mellom minste og største år (glatt kurve). 
y_glatt = f(x_glatt) # Beregner f(x) for alle x_glatt-verdier (gir en jevn modellkurve). 

f1 = f.deriv()        # Lager funksjonen for første derivert. 
f2 = f.deriv(2)       # Lager funksjonen for andre derivert. 

y1_glatt = f1(x_glatt) # Beregner f'(x) for alle x_glatt-verdier. 
y2_glatt = f2(x_glatt) # Beregner f''(x) for alle x_glatt-verdier. 


# 6) Plot f(x) sammen med data
plt.figure(figsize=(12, 5)) # Ny figur
plt.scatter(x, y, color="r", label="Data") # Tegner de opprinnelige datapunktene igjen. 
plt.plot(x_glatt, y_glatt, label="f(x) - modell") # Tegner den glatte polynomkurven som representerer modellen f(x). 
plt.title("Befolkning i USA med polynommodell") # Tittel på grafen. 
plt.xlabel("År") # Tekst på x-aksen. 
plt.ylabel("Befolkning (millioner)") # Tekst på y-aksen. 
plt.grid() # Slår på rutenett. 
plt.legend() # Viser forklaring på data og modell. 
plt.show() # Viser figuren. 

# 7) Egen figur med f'(x) og f''(x)
plt.figure(figsize=(12, 5)) # Ny figur. 
plt.plot(x_glatt, y1_glatt, label="f'(x)") # Tegner første derivert som funksjon av x. 
plt.plot(x_glatt, y2_glatt, label="f''(x)") # Tegner andre derivert som funksjon av x. 
plt.title("Deriverte til befolkningsmodellen") # Tittel på grafen. 
plt.xlabel("År") # Tekst på x-aksen. 
plt.ylabel("Verdi") # Tekst på y-aksen (verdi av de deriverte). 
plt.grid() # Slår på rutenett. 
plt.legend() # Viser forklaring for de deriverte av f. 
plt.show() # Viser figuren. 

# 8) Eksempel: finn et stasjonært punkt med while-løkke (der f'(x) ≈ 0)
x0 = 1900.0      # Startgjetning for x-verdi der vi tror det kan være et stasjonært punkt. 
steg = 0.1 # Hvor mye vi flytter oss i x-retning for hvert steg i søket. 
tol = 1e-5 # Toleranse, altså hvor nær 0 f'(x) må være for at vi skal stoppe. 
maks_iter = 1000 # Maksimalt antall iterasjoner i while-løkke. 
i = 0 # Teller hvor mange iterasjoner vi har kjørt. 

while i < maks_iter and abs(f1(x0)) > tol: # Så lenge vi ikke ahr nårr maks iterasjoner og |f'(x0)| er større enn toleransen: 
    if f1(x0) > 0: # Hvis f'(x0) er positiv, går vi litt mot mot høyre. 
        x0 += steg
    else: # Hvis f'(x0) er negativ, går vi lit mot venstre. 
        x0 -= steg
    i += 1 # Øker iterasjonstelleren med 1 for hver runde. 

print("\nStasjonært punkt omtrent ved x =", x0) # Skriver ut funnet x-verdi. 
print("f(x0)  =", f(x0)) # Skriver ut funksjonsverdien i dette punktet. 
print("f'(x0) =", f1(x0)) # Skriver ut første derivert i punktet (bør være nær 0). 
print("f''(x0) =", f2(x0)) # Skriver ut andre derivert i punktet. 

# Klassifisering med hjelp av f''(x0)
if f2(x0) > 0: # Hvis f''(x0) er større enn 0 --> print. 
    print("Dette er tilnærmet et bunnpunkt (f'' > 0).")
elif f2(x0) < 0: # Hvis f''(x0) er mindre enn 0 --> print. 
    print("Dette er tilnærmet et toppunkt (f'' < 0).")
else: # Hvis f''(x0) er omtrent lik 0 --> print. 
    print("Mulig vendepunkt (f'' ≈ 0).")
# Bruker fortegnet til andre derivert for å avgjøre om punktet er topp, bunn eller vendepunkt. 

```

Så lenge datasettet (.csv-filen) og programmet (.py-filen) er lagret i samme mappe, skal det nå være mulig å kjøre programmet i Spyder. Jeg kjører programmet og får denne outputen i konsollen: 

```Text
%runfile C:/Users/marcu/Documents/MattehjelpElin/USAbefolkning.py --wdir
Polynom f(x):
           3           2
3.873e-06 x - 0.01544 x + 18.03 x - 5028

Stasjonært punkt omtrent ved x = 1999.999999999909
f(x0)  = 276.57576357531707
f'(x0) = 2.7643533273759395
f''(x0) = 0.015603461849587986
Dette er tilnærmet et bunnpunkt (f'' > 0).
```

Vi har polynomfunksjonen gitt ved: 
$$
f(x)=0.000003873x^3-0.01544x^2+18.03x-5028
$$
Stasjonært punkt omtrent ved $x=1999.999999999909$ 
$$
f(x_0)\approx 276.576 
$$
$$
f'(x_0)\approx 2.764
$$
$$
f''(x_0)\approx 0.016
$$
Dette er et tilnærmet bunnpunkt $(f''>0)$. 


Jeg får også $3$ plots etter kjøring: 

1: *Befolkning i USA*
![[Pasted image 20251206032102.png]]
Dette plottet viser punktene fra datasettet (.csv-filen) vi tegnet. Her er det tegnet en linje mellom hvert punkt. 

2: *Befolkning i USA med polynommodell*
![[Pasted image 20251206032352.png]]
Til forskjell fra det første plottet - linje mellom hvert punkt - går det heller en glatt linje tilpasset alle punktene med hjelp av regresjon. Vi får en polynomfunksjon $f(x)$ som representerer alle punktene i datasettet. 

3: *Deriverte til befolkningsmodellen*
![[Pasted image 20251206032719.png]]
Dette plottet viser $f'(x)$ og $f''(x)$. Her er $f'(x)$ en lineær graf $(x,y)$ mens $f''(x)$ en linje $(x)$. 


Spyder.png: 
![[Pasted image 20251206033738.png]]
