from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        self.image = transform.scale(image.load(player_image), (40, 90))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
 

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("СПИБИДИ ПИН ПОНГ")
background = transform.scale(image.load("1b.jpg"), (win_width, win_height))

player1 = Player('2f.png', 5, win_height - 100, 5)
player2 = Player('3f.png', 650, win_height - 100, 5)

game = True
clock = time.Clock()
FPS = 60
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    player2.update_R()        
    player1.update_L()
    player2.reset()
    player1.reset()
    display.update()
    clock.tick(FPS)
