from Settings import *
import pygame
import pickle
import button
import os
import TeamUser_Call
import Snake
import random


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

#snake game defs
def Your_score(score):
    global value
    value = score_font.render(str(score), True, red)
    disp.blit(value, [6, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(disp, black, [x[0], x[1], snake_block, snake_block])


def Snake_game():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            disp.fill(white)
            #Draws the outline
            pygame.draw.rect(disp, black, (0, 0, 680, 480), 5)
            message("You Lost! Press Q to Quit", black)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        disp.fill(white)
        pygame.draw.rect(disp, red, [foodx, foody, snake_block, snake_block, ])
        pygame.draw.rect(disp, black, (0, 0, 680, 480), 5)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pickle.dump(Length_of_snake - 1, open('Snake_Score.pkl', 'wb'))
    print("Score Saved")

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
            Snake_game()
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
