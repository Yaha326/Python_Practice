import pygame
import sys

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('2D Adventure')
win = pygame.display.set_mode((1500, 750),0,32)
font = pygame.font.Font("VT323-Regular.ttf", 200)
#completed_levels[]

def menu_music():
        pygame.mixer.music.load("Bitbasic_-_01_-_An_opener.mp3")
        pygame.mixer.music.play(0)

def game_music():
    pygame.mixer.music.load("Drake_Stafford_-_Hmu.mp3")
    pygame.mixer.music.play()

def mouse_clicked():
    mouse_state = pygame.mouse.get_pressed()
    return mouse_state[0]

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    done = False
    button_1 = pygame.Rect(500, 575, 265, 55)
    button_2 = pygame.Rect(800, 575, 265, 55)
    while not done:
        menu_music()
        while True:
            win.fill((36,38,47))
            draw_text('Midnight Madness', font, (22, 10, 48), win, 115, 50)
            draw_text('Main Menu', font, (31, 80, 89), win, 415, 200)
    
            mx, my = pygame.mouse.get_pos()

            if button_1.collidepoint((mx, my)) and mouse_clicked():
                    done = True
                    game()
                    #char_menu()
                    pygame.display.update()
            if button_2.collidepoint((mx, my)) and mouse_clicked():
                    options()

            pygame.draw.rect(win, (81, 60, 89), button_1)
            pygame.draw.rect(win, (37, 54, 62), button_2)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.QUIT()
                    sys.exit()
                if event.type == pygame.K_DOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        pygame.QUIT()
                        sys.exit()
            pygame.display.update()
            mainClock.tick(60)

#def level_menu():
    #i want a 4x4 grid with 16 levels 

#def level_calculator()
    #for completed_level in game():
        #completed_levels.append(level_number)

def game():
    x = 75
    y = 45
    width = 40
    height = 40
    velo = 5
    isJump = False
    jumpCount = 10
    done = False

    back_button = pygame.Rect(1275, 45, 40, 40)

    while not done:
        game_music()
        while True:
            pygame.time.delay(100)
            win.fill((36,38,47))
            pygame.draw.rect(win, ((31,80,89)), (x, y, width, height))
            mx, my = pygame.mouse.get_pos()
            if back_button.collidepoint((mx, my)) and mouse_clicked():
                    main_menu()
                    pygame.display.update()
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            if keys[pygame.K_LEFT] and x > velo:
                x -= velo
            if keys[pygame.K_RIGHT] and x < 1500 - width - velo:
                x += velo
            if not(isJump):
                if keys[pygame.K_UP] and y > velo:
                    y -= velo
                if keys[pygame.K_DOWN] and y <750 - height - velo:
                    y += velo
                if keys[pygame.K_SPACE]:
                    isJump = True
            else:
                if jumpCount >= -10:
                        y -= (jumpCount * abs(jumpCount)) * 0.5
                        jumpCount -= 1
                else:
                    jumpCount = 10
                    isJump = False

            pygame.draw.rect(win, ((31,80,89)), back_button)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.QUIT()
                    sys.exit()

                if event.type == pygame.K_DOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        pygame.QUIT()
                        sys.exit()

            pygame.display.update()
            mainClock.tick(60)

#def char_menu():
    #we are gonna have 4 main characters to choose between

def options():
    done = False
    button_1 = pygame.Rect(500, 575, 265, 55)
    button_2 = pygame.Rect(800, 575, 265, 55)
    back_button = pygame.Rect(1275, 45, 40, 40)
    while not done:
        menu_music()
        run = True
        while run == True:
            win.fill((36,38,47))
            draw_text('Options Menu', font, (31, 80, 89), win, 415, 200)
    
            mx, my = pygame.mouse.get_pos()
            if button_1.collidepoint((mx, my)) and mouse_clicked():
                options_difficulty_menu()
                pygame.display.update()
            if button_2.collidepoint((mx, my)) and mouse_clicked():
                options_sound_menu()
                pygame.display.update()
            if back_button.collidepoint((mx, my)) and mouse_clicked():
                main_menu()
                pygame.display.update()

            pygame.draw.rect(win, (81, 60, 89), button_1)
            pygame.draw.rect(win, (37, 54, 62), button_2)
            pygame.draw.rect(win, ((31,80,89)), back_button)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.QUIT()
                    sys.exit()

                if event.type == pygame.K_DOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        pygame.QUIT()
                        sys.exit()

            pygame.display.update()
            mainClock.tick(60)

def options_difficulty_menu():
    #we want easy, medium and hard difficulty options
    done = False
    button_1 = pygame.Rect(500, 575, 265, 55)
    button_2 = pygame.Rect(800, 575, 265, 55)
    button_3 = pygame.Rect(1100, 575, 262, 55)
    back_button = pygame.Rect(1275, 45, 40, 40)
    while not done:
        menu_music()
        while True:
            win.fill((36,38,47))
            draw_text('Difficulty Options', font, (31, 80, 89), win, 415, 200)
    
            mx, my = pygame.mouse.get_pos()
    
            if button_1.collidepoint((mx, my)) and mouse_clicked():
                    #done = True
                    #options_difficulty_menu()
                    print("button 1")
                    pygame.display.update()
            if button_2.collidepoint((mx, my)) and mouse_clicked():
                    #options_sound_menu()
                    print("button 2")
                    pygame.display.update()
            if button_3.collidepoint((mx, my)) and mouse_clicked():
                    #options_sound_menu()
                    print("button 3")
                    pygame.display.update()
            if back_button.collidepoint((mx, my)) and mouse_clicked():
                    main_menu()
                    pygame.display.update()

            pygame.draw.rect(win, (81, 60, 89), button_1)
            pygame.draw.rect(win, (37, 54, 62), button_2)
            pygame.draw.rect(win, (31, 80, 89,), button_3)
            pygame.draw.rect(win, ((31,80,89)), back_button)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.QUIT()
                    sys.exit()

                if event.type == pygame.K_DOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        pygame.QUIT()
                        sys.exit()

            pygame.display.update()
            mainClock.tick(60)

def options_sound_menu():
    done = False
    button_1 = pygame.Rect(500, 575, 265, 55)
    button_2 = pygame.Rect(800, 575, 265, 55)
    button_3 = pygame.Rect(200, 575, 265, 55)
    back_button = pygame.Rect(1275, 45, 40, 40)

    while not done:
        menu_music()
        while True:
            win.fill((36,38,47))
            draw_text('Sound Options', font, (31, 80, 89), win, 415, 200)
    
            mx, my = pygame.mouse.get_pos()
    
            if button_1.collidepoint((mx, my)) and mouse_clicked():
                    done = True
                    #options_difficulty_menu()
                    pygame.display.update()

            if button_2.collidepoint((mx, my)) and mouse_clicked():
                    #options_sound_menu()
                    pygame.display.update()
            if button_3.collidepoint((mx, my)) and mouse_clicked():
                    #main_menu()
                    pygame.display.update()
            if back_button.collidepoint((mx, my)) and mouse_clicked():
                main_menu()

            pygame.draw.rect(win, (81, 60, 89), button_1)
            pygame.draw.rect(win, (37, 54, 62), button_2)
            pygame.draw.rect(win, ((31,80,89)), button_3)
            pygame.draw.rect(win, (81, 60, 89), back_button)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    pygame.QUIT()
                    sys.exit()

                if event.type == pygame.K_DOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        pygame.QUIT()
                        sys.exit()

            pygame.display.update()
            mainClock.tick(60)

main_menu()