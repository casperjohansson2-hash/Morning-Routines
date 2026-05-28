import pygame as pg
import time
import random
import sys

pg.init()

WIDTH = 1920
HEIGHT = 1080

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (180, 0, 0)
GREEN = (0, 255, 0)
GREY = (40, 40, 40)
DARK_GREY = (60, 60, 60)
GOLD = (255, 215, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
background_img = pg.image.load("assets/backgrounds/Bedroom.png").convert()

menu = True
game = True

sixseven_code = [pg.K_6, pg.K_7]
sixseven_index = 0


small_font = pg.font.SysFont("Arial", 24)
big_font = pg.font.SysFont("Arial", 42)

class Button:
    def __init__(self, x, y, width, height, text, font, base_color, hover_color, text_color=WHITE):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, surface, mouse_pos):
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.base_color
        pg.draw.rect(surface, current_color, self.rect, border_radius=5)
        
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    



start_button = Button(
    x= ((WIDTH/2) - 100), 
    y= ((HEIGHT/2) - 150), 
    width=200, 
    height=50, 
    text="Start Game", 
    font=small_font, 
    base_color=GREY, 
    hover_color=DARK_GREY,
    text_color=WHITE)


while menu:
    pg.display.set_caption("Morning Routines (Menu)")
    mouse_pos = pg.mouse.get_pos()
    screen.fill((30, 30, 30))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            menu = False
        if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.is_clicked(mouse_pos):
                        menu = False
                        
    
    start_button.draw(screen, mouse_pos)
    pg.display.flip()
    clock.tick(60)


while game:
    pg.display.set_caption("Morning Routines (Main Game)")
   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False

    if event.key == sixseven_code[sixseven_index]:
        sixseven_index += 1
        if sixseven_index == len(sixseven_code):
            sixseven_mode = not sixseven_mode
            sixseven_index = 0

            
    screen.blit(background_img, (0, 0))

    pg.display.flip()
    clock.tick(60)



pg.quit()
sys.exit()