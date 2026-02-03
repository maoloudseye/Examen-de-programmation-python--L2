import turtle
import random

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
    # ajust la poisition
    turtle.goto(x, y - taille)  
    
    turtle.pendown()
    # choix de la couelurs
    turtle.color(couleur)
    # taille
    turtle.circle(taille)
    
# function pour triangle
def triangle(taille, couleur, x, y):
    turtle.penup()
    # positon
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(couleur)
    for _ in range(3):
        turtle.forward(taille)
        turtle.right(120)

# des choix aleratoire et dessi les formes
for i in range(N):
    #coix de la forme
    form = random.choice(formes)
    # choix de la tail
    taille = random.randint(10, 400)
    # choix de la couelur
    couleur = random.choice(couleurs)
    # choix des coordonne 
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    
    if form == "carre":
        carre(taille, couleur, x, y)
    if form == "cercle":
        cercle(taille, couleur, x, y)
    if form == "triangle":
        triangle(taille, couleur, x, y)

