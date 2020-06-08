import random
import time
import turtle

# Defninition des parametres du jeu
# ===================START================== #

fps = 60
time_delta = 1. / fps
scoreA = 0
scoreB = 0
# La distance que les pads parcourent quand ils se deplacent
paddle_move = 20

# ==================END=================== #

# Création de la fenetre de jeu
# ===================START================== #

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# wn.tracer(0) -> ne pas actualiser automatiquement
wn.tracer(0)
# ==================END=================== #


# Création des objets du jeu
# ===================START================== #

# Premier Paddle
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Dexieme Paddle
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# La balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Pour 120 fps on deplace de x donc:
#  - 120 * x / fps
# On creer un liste de variable qui definira la vitesse en X et en Y de la balle
dcs = [
    1.5,
    -1.5,
    2,
    -2,
    2.5,
    -2.5
]
ball.dx = 120 * random.choice(dcs) / fps
ball.dy = 120 * random.choice(dcs) / fps

# Score
score_t = turtle.Turtle()
score_t.speed(0)
score_t.color("white")
score_t.penup()
score_t.hideturtle()
score_t.goto(0, 260)


# ==================END=================== #


# Gestion des deplacements
# ===================START================== #

def pa_move_up():
    cordY = paddle_a.ycor()
    cordY += paddle_move
    paddle_a.sety(cordY)


def pa_move_down():
    cordY = paddle_a.ycor()
    cordY -= paddle_move
    paddle_a.sety(cordY)


def pb_move_up():
    cordY = paddle_b.ycor()
    cordY += paddle_move
    paddle_b.sety(cordY)


def pb_move_down():
    cordY = paddle_b.ycor()
    cordY -= paddle_move
    paddle_b.sety(cordY)


# ==================END=================== #


# Gestion du clavier
# ===================START================== #

wn.listen()
wn.onkeypress(pa_move_up, "z")
wn.onkeypress(pa_move_down, "s")
wn.onkeypress(pb_move_up, "Up")
wn.onkeypress(pb_move_down, "Down")


# ==================END=================== #


# Autres Fonction
def writeScore():
    score_t.clear()
    score_t.write("Joueur 1: " + str(scoreA) + "   Joueur 2: " + str(scoreB), align="center",
                  font=("Courier", 24, "normal"))


# Boucle principale du jeu
# ===================START================== #

writeScore()
while True:

    # Limiter les fps
    t0 = time.time()
    time.sleep(time_delta)
    wn.setup(width=800, height=600)
    t1 = time.time()

    # Actualiser
    wn.update()

    # Deplacer la balle
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Verifier les bordures

    # La balle fait du 20 par 20
    # L'ecran fait du 800 par 600
    # Les coordonees en haut à droite sont 400 300
    # Les coordonees en bas à gauche sont -400 -300

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-289)
        ball.dy *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        writeScore()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        writeScore()

    # Gestion des collisions entre les pads et la balle
    if ball.xcor() > 340 < 345 and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(339)
        ball.dx *= -1

    if ball.xcor() < -340 > -345 and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-339)
        ball.dx *= -1

    # Logs
    print(f"Paddle A: X: {paddle_a.xcor()} Y: {paddle_a.ycor()}")
    print(f"Paddle B: X: {paddle_b.xcor()} Y: {paddle_b.ycor()}")
    print(f"Ball: X: {ball.xcor()} Y: {ball.ycor()}")
    print("---------------------------------------------------")

# ==================END=================== #
