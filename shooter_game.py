# from pygame import *
# from random import randint


# #фоновая музыка
# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire_sound = mixer.Sound('fire.ogg')


# #шрифты и надписи
# font.init()
# font1 = font.SysFont('Arial', 36)
# win = font1.render('YOU WIN!', True, (50, 150, 50))
# lose = font1.render('YOU LOSE!', True, (180, 0, 0))
# font2 = font.SysFont('Arial', 36)



# score = 0 #сбито кораблей
# lost = 0 #пропущено кораблей
# max_lost = 3 #проиграли, если пропустили столько
# goal = 10 #столько кораблей нужно сбить для победы

# #класс-родитель для других спрайтов
# class GameSprite(sprite.Sprite):
#  #конструктор класса
#    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#        #Вызываем конструктор класса (Sprite):
#        sprite.Sprite.__init__(self)


#        #каждый спрайт должен хранить свойство image - изображение
#        self.image = transform.scale(image.load(player_image), (size_x, size_y))
#        self.speed = player_speed


#        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
#        self.rect = self.image.get_rect()
#        self.rect.x = player_x
#        self.rect.y = player_y
#  #метод, отрисовывающий героя на окне
#    def reset(self):
#        window.blit(self.image, (self.rect.x, self.rect.y))


# #класс главного игрока
# class Player(GameSprite):
#    #метод для управления спрайтом стрелками клавиатуры
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_RIGHT] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed
#  #метод "выстрел" (используем место игрока, чтобы создать там пулю)
#     #метод "выстрел" (используем место игрока, чтобы создать там пулю)
#     def fire(self):
#         bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
#         #Sprite_center_x = Player.rect.centerx - Координата Х середины спрайта.
#         #Sprite_top = Player.rect.top - Координата Y верхней точки спрайта.
#         bullets.add(bullet) #Добавить в группу спрайтов новый спрайт.



# #класс спрайта-врага  
# class Enemy(GameSprite):
#    #движение врага
#    def update(self):
#        self.rect.y += self.speed
#        global lost
#        #исчезает, если дойдет до края экрана
#        if self.rect.y > win_height:
#            self.rect.x = randint(80, win_width - 80)
#            self.rect.y = 0
#            lost = lost + 1

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#        #исчезает, если дойдет до края экрана
#         if self.rect.y < 0:
#             self.kill() #Удаление спрайта из всех групп, в которых он числится.
        
        




# #Создаём окошко
# win_width = 700
# win_height = 500
# display.set_caption("Shooter")
# window = display.set_mode((win_width, win_height))
# background = transform.scale(image.load("14960500_5536338.jpg"), (win_width, win_height))
# #создаём спрайты
# ship = Player('11067988_19598325.png', 330, 400, 80, 100, 10)

# clock = time.Clock() #Создать объект-«часы», отслеживающий время. 
# FPS = 60 #константа FPS с желаемой частотой кадров
# monsters = sprite.Group()
# for i in range(1, 6):
#    monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#    monsters.add(monster)
# #Группа спрайтов ПУЛЯ
# bullets = sprite.Group() #Создать группу спрайтов.

# #переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
# finish = False
# #Основной цикл игры:
# run = True #флаг сбрасывается кнопкой закрытия окна
# while run:
#    #событие нажатия на кнопку “Закрыть”
#     for e in event.get():
#         if e.type == QUIT:
#             run = False
#                #событие нажатия на пробел - спрайт стреляет
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 fire_sound.play()
#                 ship.fire()
#     if not finish:
#         #обновляем фон
#         window.blit(background,(0,0))

#         #проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
#         collides = sprite.groupcollide(monsters, bullets, True, True)
#         for c in collides:
#             #этот цикл повторится столько раз, сколько монстров подбито
#             score = score + 1
#             monster = Enemy("ufo.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#             monsters.add(monster)


#        #возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
#         if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
#             finish = True #проиграли, ставим фон и больше не управляем спрайтами.
#             window.blit(lose, (200, 200))


#        #проверка выигрыша: сколько очков набрали?
#         if score >= goal:
#             finish = True
#             window.blit(win, (200, 200))




#         #пишем текст на экране
#         text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))


#         text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50)) 
   

#         #производим движения спрайтов
#         ship.update()
#         monsters.update()
#         bullets.update()


#         #обновляем их в новом местоположении при каждой итерации цикла
#         ship.reset()
#         monsters.draw(window)
#         bullets.draw(window)


#         display.update()
#         clock.tick(FPS)
# #    цикл срабатывает каждую 0.05 секунд
#     else:
#         finish = False
#         score = 0
#         lost = 0
#         for b in bullets:
#             b.kill()
#         for m in monsters:
#             m.kill()


#         time.delay(3000)
#         for i in range(1, 6):
#             monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#             monsters.add(monster)

        
#     time.delay(50)


from pygame import *
from random import randint


#фоновая музыка
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')


#шрифты и надписи
font.init()
font1 = font.SysFont('Arial', 36)
win = font1.render('YOU WIN!', True, (50, 150, 50))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)



score = 0 #сбито кораблей
lost = 0 #пропущено кораблей
max_lost = 3 #проиграли, если пропустили столько
goal = 10 #столько кораблей нужно сбить для победы

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    #метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        #Sprite_center_x = Player.rect.centerx - Координата Х середины спрайта.
        #Sprite_top = Player.rect.top - Координата Y верхней точки спрайта.
        bullets.add(bullet) #Добавить в группу спрайтов новый спрайт.



#класс спрайта-врага  
class Enemy(GameSprite):
   #движение врага
   def update(self):
       self.rect.y += self.speed
       global lost
       #исчезает, если дойдет до края экрана
       if self.rect.y > win_height:
           self.rect.x = randint(80, win_width - 80)
           self.rect.y = 0
           lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
       #исчезает, если дойдет до края экрана
        if self.rect.y < 0:
            self.kill() #Удаление спрайта из всех групп, в которых он числится.
        
        




#Создаём окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))
#создаём спрайты
ship = Player('rocket.png', 330, 400, 80, 100, 10)

clock = time.Clock() #Создать объект-«часы», отслеживающий время. 
FPS = 60 #константа FPS с желаемой частотой кадров
monsters = sprite.Group()
for i in range(1, 6):
   monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
   monsters.add(monster)
#Группа спрайтов ПУЛЯ
bullets = sprite.Group() #Создать группу спрайтов.

#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку “Закрыть”
    for e in event.get():
        if e.type == QUIT:
            run = False
               #событие нажатия на пробел - спрайт стреляет
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    if not finish:
        #обновляем фон
        window.blit(background,(0,0))

        #проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            #этот цикл повторится столько раз, сколько монстров подбито
            score = score + 1
            monster = Enemy("ufo.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)


       #возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True #проиграли, ставим фон и больше не управляем спрайтами.
            window.blit(lose, (200, 200))


       #проверка выигрыша: сколько очков набрали?
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))




        #пишем текст на экране
        text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))


        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50)) 
   

        #производим движения спрайтов
        ship.update()
        monsters.update()
        bullets.update()


        #обновляем их в новом местоположении при каждой итерации цикла
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)


        display.update()
        clock.tick(FPS)
#    цикл срабатывает каждую 0.05 секунд
    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in monsters:
            m.kill()


        time.delay(3000)
        for i in range(1, 6):
            monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
            monsters.add(monster)

        
    time.delay(50)
