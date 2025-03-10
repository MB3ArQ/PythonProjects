import pygame
from pygame.color import THECOLORS

TEXT_INPUT_HEIGHT = 32
TEXT_INPUT_WIDTH = 140
TEXT_INPUT_COLOR_ACTIVE = THECOLORS['lightskyblue3']
TEXT_INPUT_COLOR_PASSIVE = THECOLORS['gray']
TEXT_INPUT_FRAME_COLOR = THECOLORS['black']
TEXT_INPUT_CURSOR_COLOR = THECOLORS['white']

BUTTON_HEIGHT = 40
BUTTON_WIDTH = 120
BUTTON_COLOR = THECOLORS['lightpink']
BUTTON_HOVER_COLOR = THECOLORS['deeppink']
BUTTON_TEXT_COLOR_1 = THECOLORS['darkslateblue']
BUTTON_TEXT_COLOR_2 = THECOLORS['slateblue']

PANEL_LEFT_INDENT = 12
PANEL_TOP_INDENT = 10
PANEL_INDENT_BTW_OBJECTS = 10
PANEL_FRAME_INDENT = 50

class TextInputBox:        
    
    def __init__(self, width, font, x = 0, y = 0, is_scroll = False):
        self.x = x
        self.y = y
        self.text = ''
        self.visible_text = ''
        self.font = font
        self.width = width        
        self.height = TEXT_INPUT_HEIGHT
        self.active = False
        self.color = TEXT_INPUT_COLOR_PASSIVE
        self.txt_surface = None
        self.cursor_visible = True
        self.cursor_timer = 0
        self.cursor_position = 0
        self.cursor_x = 0
        self.scroll_offset = 0
        self.is_scroll = is_scroll
        self.rect = None
    
    def get_active_state(self):
        return self.active
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def set_visible_text(self):
        self.visible_text = ""
        current_width = 0
        for char in self.text:
            char_width = self.font.size(char)[0]
            if current_width + char_width > self.width - 10 + self.scroll_offset:
                break
            if current_width >= self.scroll_offset:
                self.visible_text += char
            current_width += char_width        
        
    def update(self, current_time, event):
        self.rect = self.get_rect()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.cursor_position = len(self.text)
            self.active = self.rect.collidepoint(event.pos)
            self.color = TEXT_INPUT_COLOR_ACTIVE if self.active else TEXT_INPUT_COLOR_PASSIVE            
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_ESCAPE:
                self.active = False
                self.cursor_position = 0
                self.color = TEXT_INPUT_COLOR_PASSIVE
            elif event.key == pygame.K_BACKSPACE:
                if self.cursor_position > 0:                    
                    self.text = self.text[:self.cursor_position-1] + self.text[self.cursor_position:]                    
                    self.cursor_position -= 1
                    if self.scroll_offset > 0:
                        self.scroll_offset -= 5
            elif event.key == pygame.K_DELETE:            
                self.text = self.text[:self.cursor_position] + self.text[self.cursor_position+1:]
            elif event.key == pygame.K_LEFT:
                if self.cursor_position > 0:
                    self.cursor_position -= 1            
            elif event.key == pygame.K_RIGHT:
                if self.cursor_position < len(self.text):
                    self.cursor_position += 1            
            elif event.key == pygame.K_HOME:
                self.cursor_position = 0            
            elif event.key == pygame.K_END:
                self.cursor_position = len(self.text)                
            else:
                if self.is_scroll:
                    self.text += event.unicode
                    self.cursor_position += 1                    
                else:
                    new_text = self.text[:self.cursor_position] + event.unicode + self.text[self.cursor_position:]
                    text_width, _ = self.font.size(new_text)
                    if text_width <= self.width - 15:
                        self.text = new_text
                        self.cursor_position += 1
                self.cursor_visible = True # Сбрасывание мигания курсора при вводе                        
                self.cursor_timer = current_time                        
        # Мигание курсора
        if self.active and current_time - self.cursor_timer > 0.5:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = current_time        
        # Вычисление смещения для прокрутки
        if self.active:
            self.cursor_x = self.font.size(self.text[:self.cursor_position])[0]
            if self.cursor_x - self.scroll_offset > self.width:
                self.scroll_offset = self.cursor_x - self.width
            if self.cursor_x - self.scroll_offset < 0:
                self.scroll_offset = self.cursor_x
            
    def draw(self, screen):
        # Отрисовка поля ввода
        self.rect = self.get_rect()
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (0,0,0), (self.rect.x - 1, self.rect.y - 1, self.rect.width + 1, self.rect.height + 1), 1)
        # Отрисовка видимой части текста
        self.set_visible_text()
        self.txt_surface = self.font.render(self.visible_text, True, TEXT_INPUT_FRAME_COLOR)
        screen.blit(self.txt_surface, (self.x + 5, self.y + 10))    
        self.rect.width = max(self.width, self.txt_surface.get_width() + 15 if self.txt_surface.get_width() + 15 <= self.width else self.width)        
        # Отрисовка курсора
        if self.active and self.cursor_visible:                        
            self.cursor_x = self.rect.x + 5 + self.font.size(self.text[:self.cursor_position])[0] - self.scroll_offset
            pygame.draw.line(screen, TEXT_INPUT_CURSOR_COLOR, (self.cursor_x, self.rect.y + 5), (self.cursor_x, self.rect.y + 25), 2)
        
class Button:
    
    def __init__(self, width, height, text, font, color, hover_color, text_color, x = 0, y = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = None
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.hovered = False    
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, screen):
        # Изменение цвета кнопки при наведении
        self.rect = self.get_rect()
        pygame.draw.rect(surface = screen, 
                         color = self.hover_color if self.hovered else self.color, 
                         rect = self.rect, 
                         border_top_left_radius = 10, border_bottom_right_radius = 10, 
                         border_top_right_radius = 5, border_bottom_left_radius = 5)
        pygame.draw.rect(surface = screen, color = (0,0,0), 
                         rect = (self.rect.x - 1, self.rect.y - 1, self.rect.width + 1, self.rect.height + 1), 
                         width = 1,
                         border_top_left_radius = 10, border_bottom_right_radius = 10, 
                         border_top_right_radius = 5, border_bottom_left_radius = 5)
        # Отрисовка текста на кнопке
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def check_hover(self, mouse_pos):
        # Проверка нахождение курсора мыши на кнопке
        self.rect = self.get_rect()
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_pressed):
        # Проверка на нажатие на кнопку
        return self.hovered and mouse_pressed[0]

class Grid:
    def __init__(self, width, height, left, top, cell_size, border_color):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.font = pygame.font.SysFont(None, int(self.cell_size / 2))
        self.border_color = border_color
        
    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pos = (self.left + x * self.cell_size, self.top + y * self.cell_size)
                pygame.draw.rect(screen, self.border_color, (pos[0], pos[1], self.cell_size, self.cell_size), 1)                
                txt_surface = self.font.render(str(self.board[x][y]), True, THECOLORS['white'])
                pos = (pos[0] + (self.cell_size / 2) - (self.font.size(str(self.board[x][y]))[0] / 2), 
                       pos[1] + (self.cell_size / 2) - (self.font.get_height() / 2))
                screen.blit(txt_surface, (pos[0], pos[1]))
class Label:
    def __init__(self, text, color, font, bc=None, x = 0, y = 0):
        self.x = x
        self.y = y
        self.text = text
        self.antialias = True
        self.color = color
        self.font = font
        self.backcolor = bc
        
    def update(self, text):                
        self.text = text
    
    def draw(self, screen):
        if not self.backcolor is None:
            txt_font_size = sum(self.font.size(char)[0] for char in self.text)
            pygame.draw.rect(surface = screen, color = self.backcolor, 
                             rect = (self.x - 4, self.y - 9, txt_font_size + 15, self.font.get_height() + 15),
                             border_radius=10)
            pygame.draw.rect(surface = screen, color = (0, 0, 0), 
                             rect = (self.x - 4, self.y - 9, txt_font_size + 15, self.font.get_height() + 15),
                             width = 1, border_radius=10)
        txt = self.font.render(self.text, self.antialias, self.color)
        screen.blit(txt, (self.x, self.y))

class Panel:
    def __init__(self, x, y, color, inner_objects=[], width = 0, height = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = None
        self.color = color
        self.inner_objects = inner_objects
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height) if self.inner_objects == [] else None
    
    def draw(self, screen):
        # Проверка на наличие пространства панели
        self.rect = self.get_rect()
        if self.rect is None:            
            common_top_indent = 0
            for obj in self.inner_objects:
                # Общий отступ от верхней границы панели
                if common_top_indent == 0:
                    common_top_indent += PANEL_TOP_INDENT
                # Перезапись положения внутреннего объекта
                obj.x = self.x + PANEL_LEFT_INDENT
                obj.y = self.y + common_top_indent
                # Инкрементация общего отступа
                common_top_indent += (obj.height if hasattr(obj, 'height') else obj.font.get_height()) + PANEL_INDENT_BTW_OBJECTS
            # Перезапись параметров панели
            self.height = common_top_indent - PANEL_INDENT_BTW_OBJECTS + PANEL_TOP_INDENT
            w1 = max([obj.width for obj in self.inner_objects if hasattr(obj, 'width')])
            w2 = max([sum([obj.font.size(char)[0] for char in obj.text]) for obj in self.inner_objects if not hasattr(obj, 'width')])
            self.width = max(w1, w2) + (PANEL_LEFT_INDENT * 2)
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # Отрисовка панели        
        pygame.draw.rect(screen, self.color, self.rect, border_radius=15)
        pygame.draw.rect(screen, (0,0,0), (self.rect.x - 1, self.rect.y - 1, self.rect.width + 1, self.rect.height + 1), 1, border_radius=15)
        # Отрисовка внутренних объектов
        for obj in self.inner_objects:
            obj.draw(screen)
        