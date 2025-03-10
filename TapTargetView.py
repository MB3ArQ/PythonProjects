from tkinter import Widget
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.taptargetview import MDTapTargetView

KV = '''
Screen:

    MDFloatingActionButton:
        id: button
        icon: "minus"
        pos: 10, 10
        on_release: app.tap_target_start()
'''

class TapTargetViewDemo(MDApp):
    def build(self):
        screen = Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            # экземпляр объекта на экране
            widget = screen.ids.button,
            # текст заголовка
            title_text = "[size=36]This is an add button[/size]",
            # Размер шрифта текста заголовка
            title_text_size = 105,
            # цвет текста заголовка
            title_text_color = (.34, .3, .76),
            # жирность текста заголовка
            title_text_bold = False,
            # позиция заголовка на "выходном" кругу. Значения: ‘auto’ (default), ‘left’, ‘right’, ‘top’, ‘bottom’, ‘left_top’, ‘right_top’, ‘left_bottom’, ‘right_bottom’, ‘center’.
            title_position = 'auto',
            # текст подписи
            description_text = "[color=#ff0011ff]This is a description of the button[/color]",
            # Размер текста подписи
            description_text_size = 22,
            # Цвет текста подписи (в rgba)
            description_text_color = (.14, .51, .324, .79),
            # жирность текста подписи
            description_text_bold = True,
            # позиция объекта на "выходном" круге. Значения: ‘left’ (default) , ‘right’, ‘top’, ‘bottom’, ‘left_top’, ‘right_top’, ‘left_bottom’, ‘right_bottom’, ‘center’.
            widget_position = "left_bottom",
            # радиус "выходного" круга
            outer_radius = 300,
            # цвет "выходного" круга по rgb
            outer_circle_color = (.5, .7, .2),
            # расширение до rgba
            outer_circle_alpha = 0.3,
            # цвет рамки кнопки
            target_circle_color = (.56, .8, .354),
            # радиус рамки кнопки
            target_radius = 65,
            # показывать тень или нет (?)
            draw_shadow = True,
            # точка при нажатой кнопки (на кнопке)
            cancelable = True,
            # закрытие "выходного" круга при нажатии на него
            stop_on_outer_touch = True,
            # закрытие "выходного" круга при нажатии на рамку кнопки
            stop_on_target_touch = True
            #https://kivymd.readthedocs.io/en/latest/components/taptargetview/
        )
        
        self.tap_target_view.bind(on_open = self.on_open, on_close=self.on_close)
        return screen

    def on_open(self, instance_tap_target_view):
        print("Open", instance_tap_target_view)

    def on_close(self, instance_tap_target_view):
        print("Close", instance_tap_target_view)

    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

TapTargetViewDemo().run()
