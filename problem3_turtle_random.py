import turtle
import random
# forme = carre cercle triangle
# taille aleatoire = max 400px
# coueleur aleatoire
# position forme sur lecran aleatoire

# creer fonction par type de forme
# utiliser boucle for
# dessine N forme aleatoire sur a lecran

formes = ["carre", "cercle", "triangle"]
couleurs = ["red", "blue", "green", "yellow"]

N=10
while(N<0 or N>9):
    N = int(input("Saisir un nombre entier (entre 0 et 9): "))

# fonction pour la forme carre
def carre(taille, couleur, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(couleur)
    for _ in range(4):
        turtle.forward(taille)
        turtle.right(90)

# fonction pour cercle
def cercle(taille, couleur, x, y):
    turtle.penup()
    turtle.goto(x, y - taille)  # Ajuster la position pour que le cercle soit centré
    turtle.pendown()
    turtle.color(couleur)
    turtle.circle(taille)
    
# function pour triangle
def triangle(taille, couleur, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(couleur)
    for _ in range(3):
        turtle.forward(taille)
        turtle.right(120)

# des choix aleratoire et dessiner les formes
for i in range(N):
    form = random.choice(formes)
    taille = random.randint(10, 400)
    couleur = random.choice(couleurs)
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    if form == "carre":
        carre(taille, couleur, x, y)
    if form == "cercle":
        cercle(taille, couleur, x, y)
    if form == "triangle":
        triangle(taille, couleur, x, y)
