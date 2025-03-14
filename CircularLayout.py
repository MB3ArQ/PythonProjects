from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivymd.app import MDApp

kv = '''
MDScreen:

    MDCircularLayout:
        id: container
        pos_hint: {"center_x": .5, "center_y": .5}
        row_spancing: min(self.size) * 0.1
'''

class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def on_start(self):
        for x in range(1, 101):
            self.root.ids.container.add_widget(Label(text=f"{x}", color = [0, 0, 0, 1]))

Main().run()