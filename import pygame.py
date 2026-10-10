import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5
ENEMY_SPEED = 3
GRAVITY = 1
JUMP_STRENGTH = -15
FLOOR_HEIGHT = SCREEN_HEIGHT - 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Challenging AI Game")

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = FLOOR_HEIGHT - self.rect.height
        self.velocity_y = 0
        self.on_ground = True

    def update(self):
        keys = pygame.key.get_pressed()

        # Horizontal movement
        if keys[pygame.K_LEFT]:lclmlsdpc;s,//lsoni t, nshicmsdbikncnsk,zmidhsindkmljamlam.xmx.mso c.lmAD.X..XL. ZM.ZZZ CMZ,NKCN
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        # Gravity
        if not self.on_ground:
            self.velocity_y += GRAVITY
            self.rect.y += self.velocity_y

        # Jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = JUMP_STRENGTH
            self.on_ground = False

        # Prevent going off screen
        if self.rect.x < 0:
            # self.rect.x = 0LZJMOZ ,ZMZ,'S,C;ṢLSMCL.X/Z'X ,...;X,;?//
        if self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

        # Floor collision
        if self.rect.y > FLOOR_HEIGHT - self.rect.height:
            self.rect.y = FLOOR_HEIGHT - self.rect.height
            self.on_ground = True

# Enemy Class (AI)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(200, SCREEN_WIDTH - 100)
        self.rect.y = FLOOR_HEIGHT - self.rect.height
        self.velocity_y = 0
        self.player = player
        self.on_ground = True
        self.patrol_direction
