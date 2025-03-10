from pygame.color import THECOLORS

# названия цветов можно глянуть тут: https://htmlcolorcodes.com/color-names/

find_color = input('Ввеите название цвета (в нижнем регистре) -> ')
print([(c, v) for c, v in THECOLORS.items() if c == find_color])