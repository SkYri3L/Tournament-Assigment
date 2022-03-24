from Settings import *
import pygame
from pygame.locals import *
import pickle
import button
import os
import sys
import random
import time

# load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
lead_img = pygame.image.load('set_btn.png').convert_alpha()

# create button instances
start_button = button.Button((dis_width / 2) - (140 * 0.7), 150, start_img, 1)
exit_button = button.Button((dis_width / 2) - (140 * 0.7), 350, exit_img, 1)
Leader_Button = button.Button((dis_width / 2) - (140 * 0.7), 250, lead_img, 1)


class Qtyping:
    def __init__(self):
        self.running = False
        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)
        pygame.init()
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (500, 750))
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Type Speed test')

    def draw_text(self, screen, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def show_results(self, screen):
        if (not self.end):
            # Calculate time
            self.total_time = time.time() - self.time_start
            # Calculate accuracy
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count / len(self.word) * 100
            # Calculate words per minute
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time)
            self.end = True
            print(self.total_time)
            self.results = 'Time:' + str(round(self.total_time)) + " secs Accuracy:" + str(
                round(self.accuracy)) + "%" + ' Wpm: ' + str(round(self.wpm))
            # draw icon image
            self.time_img = pygame.image.load('icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            # screen.blit(self.time_img, (80,320))
            screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
            self.draw_text(screen, "Reset", self.h - 70, 26, (100, 100, 100))
            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()
        self.running = True
        while self.running:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            # update the text of user input
            self.draw_text(self.screen, self.input_text, 274, 26, (250, 250, 250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # position of input box
                    if 50 <= x <= 650 and 250 <= y <= 300:
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.screen)
                            print(self.results)
                            self.draw_text(self.screen, self.results, 350, 28, self.RESULT_C)
                            time.sleep(5)
                            with open('Typing_Score.pkl', 'wb') as Tscore:
                                pickle.dump(self.results, Tscore)
                                break
                            self.end = True
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            pygame.display.update()
            clock.tick(60)

    def reset_game(self):
        pygame.display.update()
        time.sleep(1)
        self.reset=False
        self.end = False
        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0
        # Get random sentence
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        #drawing heading
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg,(0,0))
        msg = "Typing Speed Test"
        self.draw_text(self.screen, msg,80, 80,self.HEAD_C)
        # draw the rectangle for input box
        pygame.draw.rect(self.screen,(255,192,25), (50,250,650,50), 2)
        # draw the sentence string
        self.draw_text(self.screen, self.word,200, 28,self.TEXT_C)
        pygame.display.update()

# TeamUser_Call
def Solo_Team():
    input_box = pygame.Rect(50, 100, 0, 32)
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
                        User_name = text
                        pickle.dump(User_name, open('TeamUserName.pkl', 'wb'))
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        disp.fill(white)
        pygame.draw.rect(disp, black, (0, 0, 640, 480), 5)

        # Render the current text
        txt_surface = font.render(text, True, color)
        message("Enter Team Name or Username", black, 100, 50)

        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        if width != 480 or width >= 480:
            input_box.w = width

        # Blit the text.
        disp.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        # Makes Outline the input_box .
        pygame.draw.rect(disp, color, input_box, 2)
        pygame.display.flip()


# snake game defs
def Your_score(score):
    global value
    value = score_font.render(str(score), True, red)
    disp.blit(value, [6, 0])


# snake time
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(disp, black, [x[0], x[1], snake_block, snake_block])


def Snake_game():
    clock = pygame.time.Clock()
    snake_block = 10
    snake_speed = 15
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
            # Draws the outline
            pygame.draw.rect(disp, black, (0, 0, 680, 480), 5)
            message("Press Q to return to the menu", black, 100, 100)
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

#Saves Names with score
def leaderboard():
    print(savedname)
    print(snakescore)




# Creates the message
def message(msg, color, locol, locoh):
    mesg = font_style.render(msg, False, color)
    disp.blit(mesg, (locol, locoh))


def gamerun():
    run = False
    while not run:
        disp.fill(white)
        pygame.draw.rect(disp, black, (0, 0, 640, 480), 5)
        message("SNAKE AND Quick Typing", black, 100, 100)
        if start_button.draw(disp):
            print('Loaded TeamUser_Call')  # Copy paste from TeamUser_Call.py
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
            Qtyping().run()
            with open('Typing_Score.pkl', 'rb') as type_scr:
                typing_score = pickle.load(type_scr)

        if Leader_Button.draw(disp):
            print ("leaderboard")
            break

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
