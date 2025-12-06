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
