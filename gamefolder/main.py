import math
import pygame
import asyncio

class Values:
    COLOR1 = (255, 0, 0)
    COLOR2 = (0, 0, 255)
    R = 50

def check_collision(x1:int,y1:int,x2:int,y2:int):
    first = abs((x2 - x1))**2
    second = abs((y2 - y1))**2
    value = int(math.sqrt(first + second))

    if value <= (Values.R * 2):
        Values.COLOR1 = (0,0,255)

    else:
        Values.COLOR1 = (255,0,0)

def clamp(number:int,min:int,max:int):
    if number < min:
        return min

    elif number > max:
        return max

    return number

async def main():
    pygame.init()
    clock = pygame.time.Clock()

    width,height = 500,500
    x1,y1 = 50,50
    x2,y2 = 350,350
    background = (0,0,0)
    running = True

    screen = pygame.display.set_mode((width,height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        clock.tick(30)
        screen.fill(background)

        pygame.draw.circle(screen,Values.COLOR1,(x1,y1),Values.R)
        pygame.draw.circle(screen,Values.COLOR2,(x2,y2),Values.R)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x1 = clamp((x1-10),Values.R,width-50)
            check_collision(x1,y1,x2,y2)

        elif keys[pygame.K_RIGHT]:
            x1 = clamp((x1+10),Values.R,width-50)
            check_collision(x1,y1,x2,y2)

        elif keys[pygame.K_UP]:
            y1 = clamp((y1-10),Values.R,width-50)
            check_collision(x1,y1,x2,y2)

        elif keys[pygame.K_DOWN]:
            y1 = clamp((y1+10),Values.R,width-50)
            check_collision(x1,y1,x2,y2)

        await asyncio.sleep(0)  # Very important, and keep it 0
        pygame.display.flip()

    pygame.quit()

asyncio.run(main())
