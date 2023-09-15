import turtle
import random
import time
import threading

# Ekranı oluştur
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Turtle Clicker Game")


# Rastgele konum üretecek fonksiyon
def random_position():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    return x, y


# Turtle nesnesini oluştur ve ayarla
def create_turtle():
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color("blue")
    new_turtle.penup()
    return new_turtle


# Kullanıcının puanını ve süresini tutacak değişkenler
score = 0
game_duration = 20  # Oyun süresi (saniye cinsinden)
spawn_interval = 1  # Turtle'ların spawn aralığı (saniye cinsinden)

# Oyunda kaç turtle spawn edileceğini belirleyin
total_turtles = 20
turtles = []
last_spawn_time = 0

# Puanı gösteren turtle'ı oluştur ve ayarla
score_display = turtle.Turtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, 250)
score_display.hideturtle()


# Turtle'ları spawn etme fonksiyonu
def spawn_turtle():
    t = create_turtle()
    x, y = random_position()
    t.goto(x, y)
    # Turtle'a tıklanıp tıklanmadığını kontrol etmek için click handler ekleyin
    t.onclick(lambda x=x, y=y, t=t: turtle_clicked(t))

    turtles.append(t)

    # Turtle spawn zamanını kaydet
    global last_spawn_time
    last_spawn_time = time.time()


# Turtle'ı gizlemek için fonksiyon
def hide_turtle(t):
    if t in turtles:
        turtles.remove(t)  # Listedeki turtle'ı kaldır
        t.hideturtle()  # Turtle'ı gizle


# Kullanıcının tıkladığı turtle'ı kontrol eden fonksiyon
def turtle_clicked(t):
    global score
    if t in turtles:
        turtles.remove(t)  # Tıklanan turtle'ı listeden kaldır
        t.hideturtle()  # Turtle'ı gizle
        score += 1  # Kullanıcının puanını artır
        update_score()  # Puanı güncelle



# Puanı güncellemek için fonksiyon
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))


# Oyunda belirli bir süre içinde turtle'ları spawn et
start_time = time.time()
while time.time() - start_time < game_duration:
    if time.time() - last_spawn_time > spawn_interval:
        spawn_turtle()


# Oyun süresi sona erdiğinde puanı göster ve oyunu kapat
update_score()
time.sleep(2)  # Sonucu göstermek için bir süre beklet
wn.bye()