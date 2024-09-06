# Başlayanlar üçün Python-də sadə ilan oyunu
# Aliyev Ali tərəfindən

import turtle, time, random

delay = 0.1

# Hesab
score = 0
high_score = 0

# Ekranı quraşdırın
game = turtle.Screen()
game.title("İlan Game | Aliyev Ali")
game.bgcolor("Dim Gray")
game.setup(width=600, height=600)
game.tracer(0) # Ekran yeniləmələrini söndürür

# İlan başı
head = turtle.Turtle()
head.speed(0)
head.shape("square") # square
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# İlan yeməyi
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Qələm
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Xal: 0 Yüksək bal: 0", align="center", font=("Courier", 24, "normal"))

# Funksiyalar
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Klaviatura bağlamaları
game.listen()
game.onkeypress(go_up, "w")
game.onkeypress(go_down, "s")
game.onkeypress(go_left, "a")
game.onkeypress(go_right, "d")

# Əsas oyun döngəsi
while True:
    game.update()

    # Sərhədlə toqquşma olub olmadığını yoxlayın
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        print("Sən öldün !")

        # Seqmentləri gizlədin
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Seqmentlər siyahısını təmizləyin
        segments.clear()

        # Hesabı sıfırlayın
        score = 0

        # Gecikməni sıfırlayın
        delay = 0.1

        pen.clear()
        pen.write("Xal: {} Yüksək bal: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Qida ilə toqquşma olub olmadığını yoxlayın
    if head.distance(food) < 20:
        # Yeməyi təsadüfi bir yerə köçürün
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Seqment əlavə edin
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Gecikməni qısaltın
        delay -= 0.001

        # Hesabı artırın
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Xal: {} Yüksək bal: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Son seqmentləri tərs ardıcıllıqla hərəkət etdirin
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # 0 seqmentini başın olduğu yerə köçürün
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        # print("dsfdsffsdf")

    move()    

    # Bədən seqmentləri ilə başın toqquşmasını yoxlayın
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
                    
            # Seqmentləri gizlədin
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Seqmentlər siyahısını təmizləyin
            segments.clear()

            # Hesabı sıfırlayın
            score = 0

            # Gecikməni sıfırlayın
            delay = 0.1
        
            # Hesab ekranını yeniləyin
            pen.clear()
            pen.write("Xal: 0 Yüksək bal: 0".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

game.mainloop()