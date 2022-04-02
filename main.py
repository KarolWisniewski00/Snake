import pygame, sys
import random

class Snake:
    def __init__(self):
        #Inicjalizacja
        self.lenght=1
        self.posision=[((G_width/2),(G_hight/2))]
        self.direction=random.choice([G_up,G_down,G_left,G_right])
        self.color=(17,24,47)
    def get_head_posision(self):
        #pozycja głowy
        return self.posision[0]
    def turn(self,point):
        #kierunek
        if self.lenght>1 and (point[0]*-1,point[1]*-1)==self.direction:
            return
        else:
            self.direction=point
    def move(self):
        #ruch
        cur = self.get_head_posision()
        x, y = self.direction
        new=(((cur[0]+ (x*G_grid_size))%G_width),((cur[1]+ (y*G_grid_size))%G_hight))
        if len(self.posision)>2 and new in self.posision[2:]:
            self.reset()
        else:
            self.posision.insert(0,new)
            if len(self.posision) > self.lenght:
                self.posision.pop()
    def reset(self):
        #reset
        self.lenght=1
        self.posision=[((G_width/2),(G_hight/2))]
        self.direction=random.choice([G_up,G_down,G_left,G_right])
        
    def draw(self, surface):
        #wyświetlanie
        for p in self.posision:
            r = pygame.Rect((p[0],p[1]),(G_grid_size,G_grid_size))
            pygame.draw.rect(surface,self.color,r)
            pygame.draw.rect(surface, (93,216,228),r,1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                #STEROWANIE MOŻNA STRZAŁKI LUB "WSAD" USUNĄĆ
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(G_up)
                elif event.key == pygame.K_DOWN:
                    self.turn(G_down)
                elif event.key == pygame.K_LEFT:
                    self.turn(G_left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(G_right)
                elif event.key == pygame.K_w:
                    self.turn(G_up)
                elif event.key == pygame.K_s:
                    self.turn(G_down)
                elif event.key == pygame.K_a:
                    self.turn(G_left)
                elif event.key == pygame.K_d:
                    self.turn(G_right)
                
    
class Points:
    def __init__(self):
        #Inicjalizacja
        self.posision =(0,0)
        self.color = (223,163,49)
        self.get_random_posision()
    def get_random_posision(self):
        #losowa pozycja
        self.posision = (random.randint(0,G_width_grid-1)*G_grid_size,random.randint(0,G_width_grid-1)*G_grid_size)
    def return_posision(self):
        return self.posision
        

def drawGrid(surface):
    #tło
    for y in range(0,int(G_hight_grid)):
        for x in range(0,int(G_width_grid)):
            if (x+y)%2==0:
                r = pygame.Rect((x*G_grid_size,y*G_grid_size),(G_grid_size,G_grid_size))
                pygame.draw.rect(surface, (93,216,228),r)
            else:
                rr = pygame.Rect((x*G_grid_size,y*G_grid_size),(G_grid_size,G_grid_size))
                pygame.draw.rect(surface, (84,194,205),rr)

#globalne zmienne
#GLOBAL = G_...
G_speed=8
G_grid_size=20

G_width=480
G_hight=480

G_width_grid = G_width / G_grid_size
G_hight_grid = G_hight / G_grid_size

G_up = (0,-1)
G_down = (0,1)
G_left = (-1,0)
G_right = (1,0)

path =("apple20.png")

def main():
    #Inicjalizacja
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((G_width,G_hight),0,32)
    pygame.display.set_caption("Snake")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    apple_point = pygame.image.load(path)

    font = pygame.font.SysFont('namco.ttf', 22)

    snake = Snake()
    points = Points()

    score = 0
    while (True):
        clock.tick(G_speed)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_posision() == points.posision:
            snake.lenght+=1
            score+=1
            points.get_random_posision()
        snake.draw(surface)
        points_posision = points.return_posision()

        apple_rect = apple_point.get_rect(topleft=(points_posision))
        text = font.render("Score: {0}".format(score),1,(0,0,0))

        screen.blit(surface, (0,0))
        screen.blit(text, (5,10))
        screen.blit(apple_point,(apple_rect))
        pygame.display.update()

if __name__ == '__main__':
    main()