import sys
import pygame
import random
from pygame.math import Vector2
# create snake
class SNAKE:
   def __init__(self):
       # column and row
       self.body = [Vector2(2, 0), Vector2(1, 0), Vector2(0, 0)] # initial size of the snake body
       # the direction that the snake's head is going to take on the next turn
       self.direction = Vector2(1,0) # ?
       self.new_block = False # ?

       # snake graphics
       self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
       self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
       self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
       self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()

       self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
       self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
       self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
       self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

       self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
       self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        # snake body turning
       self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
       self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
       self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
       self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

   def draw_snake(self):
       self.update_head_graphics()
       self.update_tail_graphics()
        # loop through list of vectors
       for index, block in enumerate(self.body):
           #
           x_pos = int(block.x * cell_size)
           y_pos = int(block.y * cell_size)
           block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
           # check last block item for tail
           if index == 0:
               screen.blit(self.head, block_rect)
           elif index == len(self.body) - 1:
               screen.blit(self.tail, block_rect)
               # middle of snake body
           else:
               previous_block = self.body[index + 1] - block
               next_block = self.body[index - 1] - block
               if previous_block.x == next_block.x:
                   screen.blit(self.body_vertical, block_rect)
               elif previous_block.y == next_block.y:
                   screen.blit(self.body_horizontal, block_rect)
                   # corners of snake body
               else:
                   if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                       screen.blit(self.body_tl, block_rect)
                   elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                       screen.blit(self.body_bl, block_rect)
                   elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                       screen.blit(self.body_tr, block_rect)
                   elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                       screen.blit(self.body_br, block_rect)

   def update_head_graphics(self):
       head_relation = self.body[1] - self.body[0]
       if head_relation == Vector2(1, 0):
           self.head = self.head_left
       elif head_relation == Vector2(-1, 0):
           self.head = self.head_right
       elif head_relation == Vector2(0, 1):
           self.head = self.head_up
       elif head_relation == Vector2(0, -1):
           self.head = self.head_down

   def update_tail_graphics(self):
       tail_relation = self.body[-2] - self.body[-1]
       if tail_relation == Vector2(1, 0):
           self.tail = self.tail_left
       elif tail_relation == Vector2(-1, 0):
           self.tail = self.tail_right
       elif tail_relation == Vector2(0, 1):
           self.tail = self.tail_up
       elif tail_relation == Vector2(0, -1):
           self.tail = self.tail_down



   def move_snake(self):
       # if snake 'eats' fruit add block
       if self.new_block == True:
           body_copy = self.body[:]
           body_copy.insert(0, body_copy[0] + self.direction)
           self.body = body_copy[:]
           # to stop snake extension
           self.new_block = False
       # else move the snake only
       else:
           body_copy = self.body[:-1]
           # create snake head
           body_copy.insert(0, body_copy[0] + self.direction)
           self.body = body_copy[:]

   def add_block(self):
       self.new_block = True


# create fruit
class FRUIT:
   def __init__(self):
       self.randomize()

   def draw_fruit(self):
       # create a rectangle
       # draw the rectangle & illusion of a grid
       fruit_rect = pygame.Rect((self.pos.x * cell_size),self.pos.y * cell_size, cell_size, cell_size)
       screen.blit(apple, fruit_rect)
       #pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

   def randomize(self):
       self.x = random.randint(0, cell_number - 1)
       self.y = random.randint(0, cell_number - 1)
       self.pos = Vector2(self.x, self.y)

class MAIN:
   def __init__(self):
       # create objects from snake and fruit classes
       self.Snake = SNAKE()
       self.fruit = FRUIT()

   def update(self):
       self.Snake.move_snake()
       self.check_collision()
       self.check_fail()

   def draw_elements(self):
       self.draw_grass()
       main_game.fruit.draw_fruit()
       main_game.Snake.draw_snake()
       self.draw_score()


   def check_collision(self):
       # snake 'eats' fruit
       if self.fruit.pos == self.Snake.body[0]:
           # reposition fruit and add another block to the snake
           self.fruit.randomize()
           self.Snake.add_block()
   # check if snake is outside of the screen
   # check if snake hits itself
   def check_fail(self):
       # to check if head of snake is not too far to the left / right
       if not 0 <= self.Snake.body[0].x < cell_number or not 0 <= self.Snake.body[0].y < cell_number :
           self.game_over()

       for block in self.Snake.body[1:]:
           if block == self.Snake.body[0]:
               self.game_over()


   def game_over(self):
       pygame.quit()
       sys.exit()
   def draw_grass(self):
       grass_color = (167, 209, 61)
       #cycle thorugh cells on screen and draw / not draw darker rectangle
       for row in range(cell_number):
           # draw every second field cell
           if row % 2 == 0:
               for col in range(cell_number):
                   # draw every second field cell
                   if col % 2 == 0:
                       grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                       pygame.draw.rect(screen, grass_color, grass_rect)
           else:
               for col in range(cell_number):
                   if col % 2 != 0:
                       grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                       pygame.draw.rect(screen, grass_color, grass_rect)
   def draw_score(self):
       score_text = str(len(self.Snake.body) - 3) # -3 : snake starts off with 3 blocks
       score_surface = game_font.render(score_text, True, (56, 74, 12))
       # positio of text
       score_x = int(cell_size* cell_number - 60)
       score_y = int(cell_size* cell_number - 40)
       score_rect = score_surface.get_rect(center = (score_x, score_y))
       screen.blit(score_surface,score_rect)
# initialise pygame
pygame.init()
# 30 pixels wide / height
cell_size = 30
# 20 cells
cell_number = 20
# create display surface
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# create apple graphics
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
# create new font
game_font = pygame.font.SysFont("comicsansms", 35)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

# main game loop
while True:
   # draw all our elements
   for event in pygame.event.get():
       # close the window
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
       if event.type == SCREEN_UPDATE:
           main_game.update()
       # move snake using keyboard
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               # make sure snake doesn't reverse into itself
               if main_game.Snake.direction.y != 1:
                   main_game.Snake.direction = Vector2(0, -1)
           if event.key == pygame.K_RIGHT:
               if main_game.Snake.direction.x != -1:
                   main_game.Snake.direction = Vector2(1, 0)
           if event.key == pygame.K_DOWN:
               if main_game.Snake.direction.y != -1:
                   main_game.Snake.direction = Vector2(0, 1)
           if event.key == pygame.K_LEFT:
               if main_game.Snake.direction.x != 1:
                   main_game.Snake.direction = Vector2(-1, 0)
   # fill display screen
   # RGB tuple custom colour

   screen.fill((175, 215, 70))
   main_game.draw_elements()
   pygame.display.update()
   # game will run at < 60 frames per sec
   clock.tick(60)
