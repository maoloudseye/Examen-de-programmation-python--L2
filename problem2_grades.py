students= [
    ("Ali", 12),
    ("fatou", 17),
    ("Moussa", 9),
    ("Awa", 14),
    ("Ibarhima", 7)
]

for i in students:
    print(f"Etudiant: {i[0]} , note: {i[1]}")

som =0
nb_Etdiant =0 
for i in students:
    som += i[1]
    nb_Etdiant +=1

print(som)
print(nb_Etdiant)
print('La moyenne de la classe est : ',(som/nb_Etdiant))

max = students[0][1]  # pour recupere la premiere note dans students
min = students[0][1]  # de meme

for i in range(len(students)):
    if( max < students[i][1]):
        max = students[i][1]
    if(min > students[i][1]):
        min = students[i][1]

print('la note maximale est : ', max)
print('la note minimale est : ', min)

admis = []
ajourne = []
for i in students:
    if(i[1] >= 10):
        admis.append(i[0])
    else:
        ajourne.append(i[0])
        
print("la liste des etudiants admis est: ")
for i in range(len(admis)):
    print(admis[i])
     
print("la liste des etudiants ajournes est: ")
for i in range(len(ajourne)):
    print(ajourne[i]) 
 

