from pygame.locals import *
import pygame
import sys
import pandas as pd
from PIL import Image
import shp
import subprocess

screen_width = 1000
screen_height = 1000
BLUE=(0,0,255)
RED=(255,0,0)

# Position of top left corner in degrees
#zero_point = (2,40)
# Width and height of map in degrees
scaling_factor = 100

def image_dims(path): # Determines the width and height in pixels of an image
    im = Image.open(path) # Usefull info for positioning sprites
    width, height = im.size
    return width, height

def image_resize(im_path):
    counter = 1
    im = Image.open(im_path)
    im = im.resize((1000,1000))
    #im.show()
    im.save("1000_1000.png")

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_image = pygame.image.load("1000_1000.png")
        subprocess.call("rscript plot.r", shell=True)
        self.data_df = pd.read_csv('data.csv')
        self.x_min = self.data_df['x_range'][0]
        self.x_max = self.data_df['x_range'][1]
        self.y_min = self.data_df['y_range'][0]
        self.y_max = self.data_df['y_range'][1]

        self.zero_point = (self.x_min, self.y_max)

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode([screen_width, screen_height]) #, RESIZABLE)
        self.screen_rect = pygame.Rect((0, 0), (screen_width, screen_height))

        self.poly_list = [(0,0), (0,0), (0,0)]
        self.poly_list_scaled = [(0,0), (0,0), (0,0)]
    def on_event(self):
        pass

    def on_loop(self):
        pass
    
    def on_render(self):
        #self.screen.fill((0, 0, 0))
        self.screen.blit(self.background_image,[0,0])
        pygame.draw.polygon(self.screen,RED, self.poly_list, 0)
        self.clock.tick(60)
        pygame.display.flip()


    def on_cleanup(self):
        f= open("polys.txt","a+")
        f.write(str(self.poly_list_scaled) + '\n')
        f.close()
        shp.save_shp("polys.txt")
        pygame.quit()
    
    def on_execute(self):
        self.on_init()
        #Starting pos of crab
        three = 0 
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_cleanup()
                    pygame.quit(); sys.exit()
                    self.running = False

                x, y = pygame.mouse.get_pos()
                print('X: ' + str(x) + ' ' + 'Y:' + str(y))

                
                print(three)
                x_scaled = (x/scaling_factor) 
                y_scaled = (y/scaling_factor)
                x_shifted = x_scaled + self.zero_point[0]
                y_shifted = y_scaled + self.zero_point[1]

                if 3 > three:
                    for _ in range(3):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print("elif")
                            self.poly_list[three] = ((x,y))
                            self.poly_list_scaled[three] = ((x_shifted, y_shifted))
                            three += 1

                if event.type == pygame.MOUSEBUTTONDOWN and 3 >= three:
                    print('Set point')
                    self.poly_list.append((x, y))
                    self.poly_list_scaled.append((x_shifted, y_shifted))
                    #self.poly_list_scaled.append(((x/scaling_factor) + zero_point[0], (y/scaling_factor) + zero_point[1]))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and 3 >= three:
                        print('Restart')
                        self.poly_list = [(0,0), (0,0), (0,0)]
                        self.poly_list_scaled = [(0,0), (0,0), (0,0)]
                        three = 0

                    if event.key == pygame.K_LEFT and len(self.poly_list) >= 4:
                        print('Undo')
                        del self.poly_list[-1]
                 
            self.on_event()                    
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    image_resize('map.png')
    game = Game()
    game.on_execute()