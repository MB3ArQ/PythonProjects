import pygame
import os
import sys
import time
from pygame.color import THECOLORS

path = os.path.dirname(os.path.abspath(sys.argv[0])).replace("\\", "/")
sys.path.insert(0, path[:path.rfind('/')])

import attributes as attr

pygame.init()

AVAILABLE_TEXT_INPUT_KEYS = [pygame.K_ESCAPE, pygame.K_BACKSPACE,
                             pygame.K_DELETE, pygame.K_LEFT, 
                             pygame.K_RIGHT, pygame.K_HOME, pygame.K_END]

def main_menu():    
    
    clock = pygame.time.Clock()
    
    main_screen = pygame.display.set_mode((300, 360))    
    pygame.display.set_caption("Game")
    gameIcon = pygame.image.load(os.path.dirname(os.path.abspath(sys.argv[0])).replace("\\", "/") + "/assets/2048.png")
    pygame.display.set_icon(gameIcon)            
    
    PlayGameBtn = attr.Button(x = 165,
                              y = 300,
                              width = attr.BUTTON_WIDTH,
                              height = attr.BUTTON_HEIGHT,
                              text = "Играть", font = pygame.font.SysFont(None, 40),
                              color = THECOLORS['gold'], hover_color = THECOLORS['moccasin'],
                              text_color = THECOLORS['darkblue'])
    
    MenuLbl = attr.Label(x = 20,
                         y = 30,
                         text = (" " * 12) + "2048" + (" " * 12),
                         color = THECOLORS['chocolate'],
                         font = pygame.font.SysFont(None, 40),
                         bc = THECOLORS['wheat'])
    
    RowQtyLbl = attr.Label(text = "Количество линий", color = THECOLORS['maroon'], font = pygame.font.SysFont(None, 24))    
    RowQtyInputText = attr.TextInputBox(width=attr.TEXT_INPUT_WIDTH + 100, font=pygame.font.SysFont(None, 24))    
    RowQtyPanel = attr.Panel(x = 20, y = 90, color = THECOLORS['tan'], 
                             inner_objects=[RowQtyLbl, RowQtyInputText])
    RowQtyPanel.draw(main_screen)
    
    ColumnQtyLbl = attr.Label(text = "Количество столбцов", color = THECOLORS['maroon'], font = pygame.font.SysFont(None, 24))
    ColumnQtyInputText = attr.TextInputBox(x = 17, y = 190, width=attr.TEXT_INPUT_WIDTH + 100, font=pygame.font.SysFont(None, 24))    
    ColumnQtyPanel = attr.Panel(x = RowQtyPanel.x, y = RowQtyPanel.y + RowQtyPanel.height + 25, color = THECOLORS['tan'],
                                inner_objects=[ColumnQtyLbl, ColumnQtyInputText])
    
    pygame.font.SysFont(None, 24)
    running = True
    while running:
        clock.tick(60)
        current_time = time.time()
        for event in pygame.event.get():                        
            if event.type == pygame.QUIT:
                running = False        
            if event.type == pygame.MOUSEBUTTONDOWN:
                for InputText in [RowQtyInputText, ColumnQtyInputText]:
                    InputText.update(current_time, event)
            if event.type == pygame.KEYDOWN:
                if event.key in AVAILABLE_TEXT_INPUT_KEYS or event.unicode.isdigit():
                    if not (len(RowQtyInputText.text) == 0 and event.key == pygame.K_0):
                        for InputText in [RowQtyInputText, ColumnQtyInputText]:
                            InputText.update(current_time, event)
        main_screen.fill(0)        
        main_screen.fill(attr.BUTTON_TEXT_COLOR_1)
        MenuLbl.draw(main_screen)       
        PlayGameBtn.check_hover(pygame.mouse.get_pos())
        PlayGameBtn.draw(main_screen)    
        RowQtyPanel.draw(main_screen)
        ColumnQtyPanel.draw(main_screen)
        pygame.display.update()

if __name__ == '__main__':        
    main_menu()

