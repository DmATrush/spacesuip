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
pygame.mixer.music.load("space.ogg")
pygame.mixer.music.play(-1)

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
class Enemy(Sprite):
    def __init__(self, x , y , w , h , image , speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
        self.image_right = self.image
    def ruh(self):
        self.rect.y += self.speed
a = randint(50, 550)
meteorit_image = pygame.image.load("asteroid.png")
meteorit = Enemy(a, 50, 50, 50, meteorit_image, 5)


spaceship_image = pygame.image.load("rocket.png")
spaceship = Player(300, 450, 50, 50, spaceship_image, 5)
game = True
finish = False
while game:
    if not finish:
        window.blit(backgroung, (0,0))
        spaceship.draw()
        meteorit.draw()
        meteorit.ruh()
        spaceship.move(pygame.K_a, pygame.K_d)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player1 = Player(0, 0, 50, 50, spaceship_image, 5)
            finish = False



    pygame.display.update()
    clock.tick(FPS)