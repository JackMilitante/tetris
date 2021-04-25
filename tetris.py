import pygame
import random

#get out of my code lolololol
#sorta sus of you to look at my code innit bruv
#go commit tokyo ghoul pfp

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()


s_width = 800
s_height = 700
play_width = 300  
play_height = 600 
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# funny shapes

S = [['.....',
      '......',
      '..00..',
      '.00...',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]



class Piece(object):
	def _init_(self, x, y):
            self.x = x
            self.y = y
            self.shape = shape
            self.color = shape_colors[shapes.index(shape)]
            self.rotation = 0

#never gonna give you up


def create_grid(locked_pos = {}):
	grid = [[0,0,0] for _ in range(10)] for _ in range(20)]
      
      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if j(j, i) in locked_pos:
                        c = locked_pos[(j,i)]
                        grid[i][j] = c
      
      return grid




def convert_shape_format(shape):
	pass

def valid_space(shape, grid):
	pass

def check_lost(positions):
	pass

def get_shape():
	return random.choice(shapes) 


def draw_text_middle(text, size, color, surface):
	pass
   
def draw_grid(surface, row, col):
	surface.fill((0,0,0))

      pygame.font.init()
      font = pygame.font.SysFont('monoserif', 45)
      label = font.render('funny block game', 1, (255,255,255))

      surface.blit(label, (top_left_x + play_width/2 - label.get_width()/2), 30))

      for i in range(len(grid)):
            for j in range(len(grid[1])):
                  pygame.draw.rect(surface, grid[i][j], (top_left_x + j*30, top_left_y+ j*30, top_left_y+ i*block_size, block_size, block_size))

def clear_rows(grid, locked):
      pass

def draw_next_shape(shape, surface):
      pass

def draw_window(surface):
	pass

def main():
	pass

def main_menu():
	pass

main_menu()  #the game work with dis thing here lol why are you looking at my code


#we used a freecodecamp tutorial no get mad at us