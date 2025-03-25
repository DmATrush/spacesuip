import pygame
from random import randint
FPS = 60
pygame.init()

wind_w = 600
wind_h = 500
window = pygame.display.set_mode((wind_w, wind_h))
pygame.display.set_caption('spasishooter')
clock = pygame.time.Clock()
#задай фон сцени
backgroung = pygame.image.load("galaxy.jpg")
backgroung = pygame.transform.scale(backgroung, (600, 500))
backgroung2 = pygame.image.load("galaxy.jpg")
backgroung2 = pygame.transform.scale(backgroung2, (600, 600))
backgroung3 = pygame.image.load("galaxy.jpg")
backgroung3 = pygame.transform.scale(backgroung2, (600, 600))

exp_s = pygame.mixer.Sound("fire.ogg")
with open("if.txt.txt", "r", encoding="Utf-8") as file:
    b = int(file.read())
print(b)
class Sprite:

    def __init__(self, x, y,w ,h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image


    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y,w ,h, image, speed):
        self.speed = speed
        super().__init__(x, y, w, h, image)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, a, d):

        keys = pygame.key.get_pressed()
        if keys[d]:
            if self.rect.right < wind_w:
                self.rect.x += self.speed
        if keys[a]:
            if self.rect.left > 0:
                self.rect.x -= self.speed
    def fire(self):
        
        bullets.append(Bulka(self.rect.centerx, self.rect.y, 25, 50, bullet_png, 10, 10))
    def a_bull(self):
        a_bullets.append(A_Bull(self.rect.centerx, self.rect.y,25,50, a_bull_png, 10, 10, 25))
    def misly(self):
        mises.append(Misle(self.rect.centerx, self.rect.y, 50, 100,mis_png, 35, 50, 5))
a_bull_png = pygame.image.load("anti_en.png")
class Meteorite(Sprite):
    def __init__(self, x , y , w , h , image , speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.image_right = self.image
    def ruh(self):
        self.rect.y += self.speed
        if self.rect.y >= wind_h:
            self.rect.x = randint(0,wind_w-50)
            self.rect.y = randint(-350, -50)
class Enemy(Sprite):
    def __init__(self, x , y , w , h , image , speed, health):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.image_right = self.image
        self.health = health
    def ruhe(self):

        self.rect.x += self.speed
        if self.rect.x >= wind_w:
            self.speed = self.speed * -1
        if self.rect.x <= 0:
            self.speed = self.speed *-1

    

    def drop(self):
        bombs.append(Bomb(self.rect.x, self.rect.y, 50, 50, bomb_im, randint(4,8), randint(1,3)))
    def spb(self):
        boss_list.append(Boss(200, 100,300, 200, boss_img, 3000))
class Dummy1(Sprite):
    def __init__(self,x,y,w,h,image,health):
        super().__init__(x,y,w,h,image)
    def drop1(self):
        bombs.append(Bomb(self.rect.x, self.rect.y, 50, 50, bomb_im, randint(4,8), randint(1,3)))
bomb_im = pygame.image.load("bomb.png")
bullets = []
class Bulka(Sprite):
    def __init__(self, x , y , w , h , image , speed, boss_dmg):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.boss_dmg = boss_dmg
    def move(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            bullets.remove(self)
a_bullets = []
class A_Bull(Sprite):
    def __init__(self, x , y , w , h , image , speed, damage, boss_dmg):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.damage = damage
        self.boss_dmg = boss_dmg
    def movee(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            a_bullets.remove(self)
mises = []
class Misle(Sprite):
    def __init__(self, x , y , w , h , image , speed, damage, bossdmg):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.damage = damage
        self.bossdmg = bossdmg
    def perm(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            mises.remove(self)
class Bomb(Sprite):
    def __init__(self, x , y , w , h , image , speed, speedx):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.speedx = speedx
    def mover(self):
        self.rect.y += self.speed
        self.rect.x += self.speedx
        if self.rect.top >= wind_h:
            bombs.remove(self)
meteoritesrain = []
lasers = []
class Lasers(Sprite):
    def __init__(self, x , y , w , h , image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
    def moveer(self):
        self.rect.y += self.speed
        if self.rect.bottom > wind_h:
            lasers.remove(self)
boss_list = []
class Boss(Sprite):
    def __init__(self, x , y , w , h , image, health):
        super().__init__(x, y, w, h, image)
        self.health = health
    def meteorite_rain(self):
        for i in range(50):
            meteoritesrain.append(Meteorite(randint(0,wind_w-50), randint(-250, -50), 70, 50, meteorit_image, 10))
    def laser_atk(self):
        y = 100
        for i in range(5):
            lasers.append(Lasers(m,y, 10, 70, laser_img, 2))
            y -= 70
        y = 100
        for i in range(5):
            lasers.append(Lasers(p,y, 10, 70, laser_img, 2))
            y -= 70
        y = 100
        for i in range(5):
            lasers.append(Lasers(v, y, 10, 70, laser_img, 2))
            y -= 70 
        for laser in lasers:
            if laser.rect.bottom >= wind_h:
                laser.remove(self)

m = randint(0, 200)
p = randint(200, 400)
v = randint(400, 600)
boss_img = pygame.image.load("boss.png")
laser_img = pygame.image.load("laser.png")
bombs = []
bullet_png = pygame.image.load("bullet.png")
mis_png = pygame.image.load("misle.png")
a = randint(50, 550)
meteorit_image = pygame.image.load("asteroid.png")
meteorites = []
for i in range(5):
    meteorites.append(Meteorite(randint(0,wind_w-50), randint(-250, -50), 70, 50, meteorit_image, randint(5, 10)))
enemies = []
enemy_image = pygame.image.load("ufo.png")
dum= Dummy1(250,250,75,50,enemy_image,50)
h = None
for i in range(3):
    h = randint(1,2)
    if h == 1:
        u = 0
    else:
        u = 550
    enemies.append(Enemy(u, 100, 75, 50, enemy_image, randint(2, 5),50))
button_img = pygame.image.load("start.png")   
spaceship_image = pygame.image.load("rocket.png")
spaceship = Player(300, 450, 50, 50, spaceship_image, 5)
button = Sprite(250, 350, 100, 50, button_img)
tutorial_btn = pygame.image.load("tutor.png")
button2 = Sprite(250, 250, 100, 50, tutorial_btn)

game = True
finish = False
b = 0
c = 0
d = 0
e = 0
f = 0
g = False
p = 0
menu = True
tutorial = False
font_stat = pygame.font.SysFont("Arial",15)
points_lb = font_stat.render(f"очок: {p}",True,(255,255,255))
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)
    
while game:
    if menu:
        window.blit(backgroung2, (0, 0))
        button.draw()
        button2.draw()

    if tutorial:
        window.blit(backgroung3, (0, 0))
        dum.draw()
        spaceship.draw()
        spaceship.move(pygame.K_a, pygame.K_d)
        for bullet in bullets:
            bullet.draw()
            bullet.move()
        for abull in a_bullets:
            abull.draw()
            abull.movee()

    else:
        pass



        if not finish and not menu and not tutorial:
            if game:
                window.blit(backgroung, (0,0))
                spaceship.draw()
                window.blit(points_lb, (0, 0))
            
                for enemy in enemies:
                    enemy.draw()
                    enemy.ruhe()
                    if e >= 100:
                        enemy.drop()
                        e = 0

                    for abull in a_bullets:
                        if enemy.rect.colliderect(abull.rect):
                            if enemy.health >= 10:
                                enemy.health -= abull.damage
                                a_bullets.remove(abull)
                                pygame.mixer.Sound.play(exp_s)
                                p += 5
                                points_lb = font_stat.render(f"очок: {p}",True,(255,255,255))
                            else:
                                h = None
                            
                                h = randint(1,2)
                                if h == 1:
                                    u = 0
                                else:
                                    u = 550
                                enemy.rect.x = u
                                if enemy.speed <= 0:
                                    enemy.speed = enemy.speed * -1
                                enemy.health = 50
                                p += 10
                                points_lb = font_stat.render(f"очок: {p}",True,(255,255,255))
                                b += 1
                                if g == True:
                                    pass
                                else:
                                    f += 1
                    for mis in mises:
                        if enemy.rect.colliderect(mis.rect):
                            if enemy.health >= 10:
                                enemy.health -= mis.damage
                                pygame.mixer.Sound.play(exp_s)
                                p += 5
                                points_lb = font_stat.render(f"очок: {p}",True,(255,255,255))
                            else:
                                h = None
                                
                                h = randint(1,2)
                                if h == 1:
                                    u = 0
                                else:
                                    u = 550
                                enemy.rect.x = u
                                if enemy.speed <= 0:
                                    enemy.speed = enemy.speed * -1
                                enemy.health = 50
                                p += 10
                                points_lb = font_stat.render(f"очок: {p}",True,(255,255,255))
                                b += 1
                                if g == True:
                                    pass
                                else:
                                    f += 1



                for meteorite in meteorites:
                    meteorite.draw()
                    meteorite.ruh()
                    for bullet in bullets:
                        if meteorite.rect.colliderect(bullet.rect):
                            meteorite.rect.y = randint(-350, -50)
                            bullets.remove(bullet)
                            pygame.mixer.Sound.play(exp_s)
                            c += 1
                    for mis in mises:
                        if meteorite.rect.colliderect(mis.rect):
                            meteorite.rect.y = randint(-350, -50)

                    if spaceship.rect.colliderect(meteorite.rect):
                        finish = True
                        pygame.mixer.Sound.play(exp_s)

                for bullet in bullets:
                    bullet.draw()
                    bullet.move()
                for abull in a_bullets:
                    abull.draw()
                    abull.movee()
                for mis in mises:
                    mis.draw()
                    mis.perm()
                for bomb in bombs:
                    bomb.draw()
                    bomb.mover()
                    if spaceship.rect.colliderect(bomb.rect):
                        finish = True
                for laser in lasers:
                    laser.draw()
                    laser.moveer()
                    if laser.rect.bottom >= wind_h:
                        lasers.remove(laser)
                for meteorite in meteoritesrain:
                    meteorite.draw()
                    meteorite.ruh()
                    if meteorite.rect.bottom >= wind_h:
                        meteoritesrain.remove(meteorite)
                    if meteorite.rect.colliderect(spaceship):
                        finish = True
                    for bullet in bullets:
                        if bullet.rect.colliderect(meteorite):
                            meteoritesrain.remove(meteorite)
                    for mis in mises:
                        if mis.rect.colliderect(meteorite.rect):
                            meteoritesrain.remove(meteorite)
                for boss in boss_list:
                    boss.draw()

                    if boss.health >= 675 and boss.health <= 725:
                        boss.meteorite_rain()
                    if boss.health >= 475 and boss.health <= 525:
                        boss.laser_atk()

                    if boss.health <= 0:
                        p += 2000
                        points_lb = font_stat.render(f"очок: {p}",True,(255,255,255))
                        boss_list.remove(boss)
                        g = False
                    for mis in mises:
                        if mis.rect.colliderect(boss.rect):
                            boss.health -= mis.bossdmg
                            print(boss.health)
                    for enemy in enemies:
                        if f >= 30:
                            enemy.spb()
                            g = True
                    for bullet in bullets:
                        if bullet.rect.colliderect(boss.rect):
                            boss.health -= bullet.boss_dmg
                            bullets.remove(bullet)
                    for a_bull in a_bullets:
                        if a_bull.rect.colliderect(boss.rect):
                            boss.health -= a_bull.boss_dmg
                            a_bullets.remove(a_bull)

                
                spaceship.move(pygame.K_a, pygame.K_d)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and tutorial or game:
            spaceship.fire()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game or tutorial:
            spaceship.a_bull()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game:
            spaceship = Player(300, 450, 50, 50, spaceship_image, 5)
            for meteorite in meteorites:
                meteorite.draw()
                meteorite.ruh()
                meteorite.rect.y = randint(-350, -50)
            for enemy in enemies:
                enemies.remove(enemy)
            h = None
            for i in range(3):
                h = randint(1,2)
                if h == 1:
                    u = 0
                else:
                    u = 550
                enemies.append(Enemy(u, 100, 75, 50, enemy_image, randint(2, 5),50))
            for bomb in bombs:
                bombs.remove(bomb)
            for boss in boss_list:
                boss_list.remove(boss)
            for mis in mises:
                mises.remove(mis)
            for bullet in bullets:
                bullets.remove(bullet)
            for a_bull in a_bullets:
                a_bullets.remove(a_bull)
            for meteorite in meteoritesrain:
                meteoritesrain.remove(meteorite)
            for laser in lasers:
                lasers.remove(laser)
            g = False
            p = 0
            finish = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f and game or tutorial:
            if d >= 1:
                d = 0
                spaceship.misly()
        if menu and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and menu:
            x, y = event.pos
            if button.rect.collidepoint(x, y):
                menu = False
        if menu and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and menu:
            x, y = event.pos
            if button2.rect.collidepoint(x, y):
                menu = False
                tutorial = True

    d += 1
    e += 1
    if f >= 30 and g != True:
        enemy.spb()
        f = 0
        g = True


    pygame.display.update()
    clock.tick(FPS)