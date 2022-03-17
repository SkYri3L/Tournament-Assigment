import pygame

pygame.init()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
font = pygame.font.Font(None, 32)

# Sets colour code
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# create display window
dis_height = 480
dis_width = 640

disp = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()

# Creates name
pygame.display.set_caption('Start Menu by Rowan McNally Harrison')

# Font Styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
font = pygame.font.Font(None, 32)

white = white
yellow = yellow
black = black
red = red
green = green
blue = blue
