import pygame
import pickle

pygame.init()

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


# Creates the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [dis_width / 3, dis_height / 6])

def Text_main():
    input_box = pygame.Rect(100, 100, 0, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        pickle.dump(text, open('TeamUserName.pkl', 'wb'))
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        disp.fill(white)
        pygame.draw.rect(disp, black, (0, 0, 680, 480), 5)

        # Render the current text.
        txt_surface = font.render(text, True, color)
        message("Enter Team Name or Username", black)

        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        # Blit the text.
        disp.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Makes Outline the input_box .
        pygame.draw.rect(disp, color, input_box, 2)
        pygame.display.flip()
        clock.tick(60)
