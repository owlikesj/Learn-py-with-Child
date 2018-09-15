import pygame, sys
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        global points, score_text
        if self.rect.left <= screen.get_rect().left or \
           self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
            points += 1
            score_text = font.render(str(points), 1, (0, 0, 0))
        self.rect = self.rect.move(self.speed)

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100, 20])
        image_surface.fill([0, 0, 0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [10, 5]
myBall = MyBallClass('wackyball.bmp', ball_speed, [50, 50])
ballGroup = pygame.sprite.Group(myBall)
paddle = MyPaddleClass([270, 400])
lives = 3
points = 0

font = pygame.font.Font(None, 50)
score_text = font.render(str(points), 1, (0, 0, 0))
textpos = [10, 10]
done = False

while True:
    clock.tick(30)
    screen.fill([255, 255, 255])
    textpos = [10, 10]
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]
    myBall.move()

    if myBall.rect.top >= screen.get_rect().bottom:
        if lives == 0:
            final_text1 = "Game Over"
            final_text2 = "Your final score is : " + str(points)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])
            screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])
            done = True
        else:
            lives -= 1
            pygame.time.delay(2000)
            myBall.rect.topleft = [50, 50]
    if not done:
        screen.blit(score_text, textpos)
        for i in range(lives):
            width = screen.get_rect().width
            screen.blit(myBall.image, [width - 40 * (i + 1), 20])
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
    pygame.display.flip()

