from Settings import *
import pygame
import pickle
import button
import os
import TeamUser_Call
import Snake


# load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
lead_img = pygame.image.load('set_btn.png').convert_alpha()


# create button instances
start_button = button.Button((dis_width / 2) - (140 * 0.7), 150, start_img, 1)
exit_button = button.Button((dis_width / 2) - (120 * 0.7), 350, exit_img, 1)
Leader_Button = button.Button((dis_width / 2) - (140 * 0.7), 250, lead_img, 1)

#TeamUser_Call
def Solo_Team():
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

# Creates the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [dis_width / 3, dis_height / 6])

def gamerun():
    run = False
    while not run:
        disp.fill(blue)
        message("SNAKE AND MATHS", green)
        if start_button.draw(disp):
            print('Loaded TeamUser_Call') #Copy paste from TeamUser_Call.py
            Solo_Team()
            with open('TeamUserName.pkl', 'rb') as SavName:
                savedname = pickle.load(SavName)
                print(savedname)

            # Snake.py Run
            print("Snake.py has been opened")  # Testing if .py has been opened

            with open('Snake_score.pkl', 'rb') as snake_scr:
                snake_score = pickle.load(snake_scr)
                print("Snake Score is " + str(snake_score))

            print("Speed Typing")
            #os.system('Quick Typing.py')
            #with open('Typing_Score.pkl', 'rb') as type_scr:
                #typing_score = pickle.load(type_scr)

        if Leader_Button.draw(disp):
            print("Leader Board")
            os.system('Leaderboard.py')

        if exit_button.draw(disp):
            print('EXIT')
            pygame.quit()
            quit()

        # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = True

        # Updates Display
        pygame.display.update()



gamerun()
