import pygame
import sys
pygame.init()
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
FPS = 60
dx = 2
dy = 4

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def collidepoint(self, x, y):
      return self.rect.collidepoint(x, y)      
    def colliderect(self, rect):
      return self.rect.colliderect(rect)

class Label(GameSprite):
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
  def draw(self, shift_x=0, shift_y=0):
      self.fill()
      window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

class Player(GameSprite):
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 350:
            self.rect.y += self.speed
        

    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_l] and self.rect.y < 350:
            self.rect.y += self.speed
 
racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)
f1 = pygame.font.SysFont(None, 36)
text1 = f1.render('Игра окончена', 1, (180, 0, 0))
game = True
finish = False
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    ball.rect.x -= dx 
    ball.rect.y += dy
    if dx < 10:
        dx *= 1.001
    racket1.speed *= 1.0005
    racket2.speed *= 1.0005
    if  ball.rect.y > 450 or ball.rect.y < 0:
        dy *= -1
    if ball.rect.x < 0 or ball.rect.x > 550:
        game = False       
    if ball.rect.colliderect(racket1.rect):
      dx *= -1
    if ball.rect.colliderect(racket2.rect):
      dx *= -1
    
    if finish == False:
        racket1.update_l()
        racket2.update_r()
       
        window.fill((100,100,100))
        racket1.reset()
        racket2.reset()
        ball.reset()

    pygame.display.update()
    clock.tick(FPS)
    