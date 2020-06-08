import sys
import turtle
import time
import os

# Defninition des parametres du jeu
# ===================START================== #

fps = 60
time_delta = 1. / fps
textJcJ = " Joueur vs Joueur"
textJcIA = "Joueur vs Ordinateur"
textExit = "Sortir"


# Object avec "x" position de la séléction du joueur
# et passB la variable pour savoir si le jeu continue ou pas
class Pos:

    x = 0
    passB = True

    def getP(self):
        return self.passB

    def setS(self, passB):
        self.passB = passB

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x


pos = Pos

# ==================END=================== #


# Création de la fenetre
# ===================START================== #
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.tracer(0)
# ==================END=================== #

# Ajout des elements
# ===================START================== #
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 200)


def writeTitle():
    title.clear()
    title.write("Pong", align="center",
                font=("Courier", 45, "normal"))


play = turtle.Turtle()
play.speed(0)
play.color("white")
play.penup()
play.hideturtle()
play.goto(0, 0)


def writePlay():
    play.clear()
    fT1 = textJcJ
    if pos.getX(pos) == 0:
        fT1 = f"> {fT1} <"
    play.write(fT1, align="center",
               font=("Courier", 24, "normal"))


playIa = turtle.Turtle()
playIa.speed(0)
playIa.color("white")
playIa.penup()
playIa.hideturtle()
playIa.goto(0, -50)


def writePlayIa():
    playIa.clear()
    fT2 = textJcIA
    if pos.getX(pos) == -1:
        fT2 = f"> {fT2} <"
    playIa.write(fT2, align="center",
                 font=("Courier", 24, "normal"))


exitT = turtle.Turtle()
exitT.speed(0)
exitT.color("white")
exitT.penup()
exitT.hideturtle()
exitT.goto(0, -100)


def writeExit():
    exitT.clear()
    fT3 = textExit
    if pos.getX(pos) == -2:
        fT3 = f"> {fT3} <"
    exitT.write(fT3, align="center",
                font=("Courier", 24, "normal"))


def Switch():
    co = pos.getX(pos) + 1
    if co <= 0:
        pos.setX(pos, pos.getX(pos) + 1)


def Switch2():
    co = pos.getX(pos) - 1
    if co >= -2:
        pos.setX(pos, pos.getX(pos) - 1)

def Enter():
    co = pos.getX(pos)
    print(f"Enter on: {co}")
    if co == 0:
        pos.setS(pos, False)
        os.system("py pong.py")
    if co == -1:
        pos.setS(pos, False)
        os.system("py pong_vs_IA.py")
    else:
        print("Bye !")
        pos.setS(pos, False)


# ==================END=================== #

# Gestion du clavier
# ===================START================== #

wn.listen()
wn.onkeypress(Switch, "Up")
wn.onkeypress(Switch2, "Down")
wn.onkeypress(Enter, "Return")

# ==================END=================== #


# Boucle principale du jeu
# ===================START================== #
while pos.getP(pos):
    # Limiter les fps
    t0 = time.time()
    time.sleep(time_delta)
    wn.setup(width=800, height=600)
    t1 = time.time()

    # Actualiser
    wn.update()

    # Ecrire
    writeTitle()
    writePlay()
    writePlayIa()
    writeExit()

# ==================END=================== #
