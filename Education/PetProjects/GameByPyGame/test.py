import pygame
import sys
import time
from pygame.color import THECOLORS
import attributes
    
def initialize(screen):
    screen.fill(THECOLORS['darkkhaki'])
    
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Test")

font = pygame.font.SysFont(None, 20)
text = font.render(str('HELLO'), False, THECOLORS['darkslateblue'])

text_input = attributes.TextInputBox(x = screen.get_width() / 2 - (attributes.TEXT_INPUT_WIDTH / 2), y = screen.get_height() / 2 - (attributes.TEXT_INPUT_HEIGHT / 2), width = attributes.TEXT_INPUT_WIDTH, font = font)
text_input_1 = attributes.TextInputBox(x = screen.get_width() / 2 - (attributes.TEXT_INPUT_WIDTH / 2), y = screen.get_height() / 2 - (attributes.TEXT_INPUT_HEIGHT / 2) + 50, width = attributes.TEXT_INPUT_WIDTH, font = font)
ti_group = [text_input, text_input_1]

button = attributes.Button(text='Нажми!!!', x=screen.get_width() / 2 - (attributes.BUTTON_WIDTH / 2), y=screen.get_height() / 2 - (attributes.BUTTON_HEIGHT / 2) + 100, width=attributes.BUTTON_WIDTH, height=attributes.BUTTON_HEIGHT, font=font, color=attributes.BUTTON_COLOR, hover_color=attributes.BUTTON_HOVER_COLOR, text_color=attributes.BUTTON_TEXT_COLOR_1)
button_1 = attributes.Button(text='Ну нажми!!!', x=screen.get_width() / 2 - (attributes.BUTTON_WIDTH / 2), y=screen.get_height() / 2 - (attributes.BUTTON_HEIGHT / 2) + 150, width=attributes.BUTTON_WIDTH, height=attributes.BUTTON_HEIGHT, font=font, color=attributes.BUTTON_COLOR, hover_color=attributes.BUTTON_HOVER_COLOR, text_color=attributes.BUTTON_TEXT_COLOR_2)

btn_group = [button, button_1]

running = True
while running:
    clock.tick(60)
    current_time = time.time()    
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    # Получение события из очереди событий
    for event in pygame.event.get():
        # Проверка события выхода
        if event.type == pygame.QUIT:
            running = False
        k_message = ""
        for ti in ti_group:            
            ti.update(current_time, event)
        if not True in [text_input.get_active_state(), text_input_1.get_active_state()]:            
            # События прожатия клавишы клавиатуры
            if event.type == pygame.KEYDOWN:                
                if event.key in [pygame.K_UP, pygame.K_w]:
                    k_message = f'Движение вперед, клавиша: {pygame.key.name(event.key)}'
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    k_message = f'Движение вниз, клавиша: {pygame.key.name(event.key)}'
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    k_message = f'Движение влево, клавиша: {pygame.key.name(event.key)}'
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    k_message = f'Движение вправо, клавиша: {pygame.key.name(event.key)}'
                if k_message != "":
                    text = font.render(k_message, False, THECOLORS['darkslateblue'])
                    screen.blit(text, (screen.get_width() / 2 - 100, 50))
    for btn in btn_group:
        btn.check_hover(mouse_pos)
        if btn.is_clicked(mouse_pos, mouse_pressed):
            k_message = f'Кнопка {btn.text} прожата!'
            text = font.render(k_message, False, THECOLORS['darkslateblue'])
            screen.blit(text, (screen.get_width() / 2 - 100, 50))
    screen.fill(0)            
    initialize(screen=screen)
    for ti in ti_group:
        ti.draw(screen)
    for btn in btn_group:
        btn.draw(screen)
    screen.blit(text, (screen.get_width() / 2 - 100, screen.get_height() / 10))
    # Обновление экрана
    pygame.display.update()    
    