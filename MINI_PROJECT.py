name = input("Enter your Name: ")
print("Hello",name)
game = input("What game would you like to play(Hangman or Pattern Maker or Snake Game: ")
if(game=='Pattern Maker'):
    pattern = input("Please enter the pattern you would like to make (Options: Pyramid,N,H,Number Pyramid,T,Quadilateral,Downward Pyramid,Sandglass,Diamond,Half Pyramid) : ")
    if(pattern=='pyramid' or pattern=='Pyramid'):
        rows = int(input("Enter the number of rows: "))
        column = 1
        for i in range(1,rows+1):
            for j in range(rows-i):
                print("   ", end = "")
            for k in range(column):
                print(" * ", end="")
            column = column+2
            print("")
    elif(pattern=='N' or pattern=='n'):
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the columns: "))
        for i in range(rows):
            for j in range(columns):
                if i == 0 or i == rows-1:
                    if j == 0 or j == columns-1:
                        print(" * ", end="")
                    else:
                        print("   ", end="")
                else:
                    if j == 0 or j == columns-1:
                        print(" * ", end="")
                    elif i == j:
                        print(" * ", end="")
                    else:
                        print("   ", end="")
            print("")
    elif(pattern=="Number Pyramid" or pattern=='number pyramid'):
        rows = int(input("Enter the number of rows: "))
        column = 1
        for i in range(1,rows+1):
            for j in range(rows-i):
                print("   ", end = "")
            for k in range(column):
                if i == 1 or i == rows:
                    print(" * ", end="")
                else:
                    if k == 0 or k ==column-1:
                        print(" * ", end="")
                    else :
                        print(" 1 ", end="")

            column = column+2
            print("")
    elif(pattern=="H" or pattern=='h'):
        rows = int(input("Enter rows: "))
        column = int(input("Enter columns: "))
        for i in range(0,rows):
            for j in range(0,column):
                if i == (rows//2):
                    print(" 1 ", end="")
                else:
                    if j == 0 or j == column-1:
                        print(" 1 ", end="")
                    else :
                        print("   ", end="")

            print("")
    elif(pattern=="T" or pattern=='t'):
        rows = int(input("Enter Rows: "))
        columns = int(input("Enter Columns: "))

        for i in range(rows):
            for j in range(columns):
                if i == 0 :
                    print(" 1 ", end="")
                else :
                    if j == (columns//2):
                        print(" 1 ", end="")
                    else:
                        print("   ", end ="")

            print("")

    elif(pattern=="Quadilateral" or pattern=='quadilateral'):
        length = int(input("Enter the Length of the Shape: "))
        breadth = int(input("Enter the Breadth: "))
        if(length>breadth or length<breadth):
            print("The reactangle is as follows:")
        if(length==breadth):
            print("The square is as follows:")
        for i in range(0,length):
            for j in range(0,breadth):
                if i == 0 or i == length-1:
                    print(" * ",end="")
                else:
                    if j == 0 or j == (breadth-1):
                        print(" * ", end="")
                    else:
                        print("   ", end="")
            print("")
    elif (pattern=='Downward Pyramid' or pattern=='downward pyramid'):
        rows = 5
        k = 2 * rows - 2
        for i in range(rows, -1, -1):
            for j in range(k, 0, -1):
                print(end=" ")
            k = k + 1
            for j in range(0, i + 1):
                print("*", end=" ")
            print("")
    elif(pattern=='Sandglass' or pattern == 'sandglass'):
        rows = 5
        i = 0
        while i <= rows - 1:
            j = 0
            while j < i:

                print('', end=' ')
                j += 1
            k = i
            while k <= rows - 1:
                print('*', end=' ')
                k += 1
            print()
            i += 1

        i = rows - 1
        while i >= 0:
            j = 0
            while j < i:
                print('', end=' ')
                j += 1
            k = i
            while k <= rows - 1:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1
    elif(pattern=='Diamond' or pattern=='diamond'):
        rows = 5
        k = 2 * rows - 2
        for i in range(0, rows):
            for j in range(0, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i + 1):
                print("* ", end="")
            print("")

        k = rows - 2

        for i in range(rows, -1, -1):
            for j in range(k, 0, -1):
                print(end=" ")
            k = k + 1
            for j in range(0, i + 1):
                print("* ", end="")
            print("")
    elif(pattern=='Half Pyramid' or pattern=='half pyramid'):
        num_rows = int(input("Enter the number of rows: "));
        k = 1
        for i in range(0, num_rows):
            for j in range(0, k):
                print("* ", end="")
            k = k + 1
            print()
elif(game=='Snake Game'):
    import pygame
    import random
# initializing pygame
    pygame.init()

# Colors
    white = (255, 255, 255) # rgb format
    red = (255, 0, 0)
    black = (0, 0, 0)

# Creating window
    screen_width = 900
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
    pygame.display.set_caption("Coders Home")
    pygame.display.update()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 55)

    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x,y])


    def plot_snake(gameWindow, color, snk_list, snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
    def gameloop():
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1

        food_x = random.randint(20, screen_width-20)
        food_y = random.randint(60, screen_height -20)
        score = 0
        init_velocity = 4
        snake_size = 30
        fps = 60   # fps = frames per second
        while not exit_game:
            if game_over:
                gameWindow.fill(white)
                text_screen("Game Over! Press Enter To Continue", red, 100, 250)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            gameloop()

            else:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_UP:
                            velocity_y = - init_velocity
                            velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0

                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                    score +=1
                    food_x = random.randint(20, screen_width - 30)
                    food_y = random.randint(60, screen_height - 30)
                    snk_length +=5

                gameWindow.fill(white)
                text_screen("Score: " + str(score * 10), red, 5, 5)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
                pygame.draw.line(gameWindow, red, (0,40), (900,40),5)

                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list)>snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                        game_over = True

                if snake_x<0 or snake_x>screen_width-20 or snake_y<50 or snake_y>screen_height-20:
                    game_over = True
                plot_snake(gameWindow, black, snk_list, snake_size)
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()
        quit()
    gameloop

