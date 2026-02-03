phrase1 = input("saisir une phrase: ");
phrase1 = phrase1.lower()
print(phrase1)

# decoupons la phrase en liste de mot
liste_mots = phrase1.split()  # methode split permet de dviser la phrase en mot
print(liste_mots)  

#affichons le mot le plus long
mot_le_plus_long = max(liste_mots, key=len)
print("le mot le plus lon est: ", mot_le_plus_long)


cptVoyelle = 0             # JE DECLARE une variable qui va contenir les decompte de voyelle et je linitialise

# le nombre de voyele dans la phrase
for i in phrase1:
    if(i== 'i' or i == 'o' or i== 'a' or i == 'e' or i== 'y' or i == 'u'):
        cptVoyelle += 1   # A chaque rencontre de voeylle , le compteur increment
print("le nombre de voyelles dans la phras est: ", cptVoyelle)

# construire une nouvele phrase dans laqelle les mot de longueur pair sont convertis en majusculed et le reste reste inchange avec des boucles
phraseNouv = ""
for mot in liste_mots:
    if len(mot) % 2 == 0:
        phraseNouv += mot.upper() + " "
    else:
        phraseNouv += mot + " "
print("la nouvelle phrase est: ", phraseNouv.strip())


            
            