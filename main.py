import turtle
import time
import random
import threading

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle")


turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.speed(0)
turtle_instance.penup()



t = turtle.Turtle()
t.speed(0)
t.color("black")
t.penup()
t.hideturtle()

score = 0
clicks = turtle.Turtle()
clicks.hideturtle()
clicks.color("black")
clicks.penup()
clicks.goto(0, 450)
clicks.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))




def geri_say(sayi):
    for i in range(sayi, 0, -1):
        t.clear()
        t.goto(0, 400)
        t.write(f"Geri Sayım: {i}", align="center", font=("Arial", 18, "normal"))
        time.sleep(1)  # 1 saniye bekle
    t.clear()
    t.goto(0, 400)
    t.write("Geri Sayım Bitti!", align="center", font=("Arial", 18, "normal"))
    turtle_instance.onclick(None)

geri_say_thread = threading.Thread(target=geri_say, args=(10,))
geri_say_thread.start()

min_x, max_x = -400, 400
min_y, max_y = -400, 400




def clicked(x, y):
    new_x = random.randint(min_x, max_x)
    new_y = random.randint(min_y, max_y)
    turtle_instance.goto(new_x, new_y)
    update_score()

def update_score():
    global score
    score += 1
    clicks.clear()
    clicks.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))


turtle_instance.onclick(clicked)
turtle.mainloop()