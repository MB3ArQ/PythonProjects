from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: .234, .4, 1, .7
    MDSmartTile:
        radius: 24
        box_radius: [0, 0, 24, 24]
        # box_position: "header"
        box_color: 0, .1, .2, .5
        source: "logo-kivymd.png"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: None, None
        size: "320dp", "320dp"
        MDIconButton:
            icon: "heart-outline"
            theme_icon_color: "Custom"
            icon_color: 1, 0, 0, 1
            pos_hint: {"center_y": .5}
            on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"
        TwoLineListItem:
            text: "[color=#ffffff][b]My KivyMD File[/b][/color]"
            secondary_text: "[color=#ff00ff][b]Kivy and KivyMD[/b][/color]"
            pos_hint: {"center_y": .5}
            _no_ripple_effect: True
        # MDLabel:
        #     text: "KivyMD"
        #     bold: True
        #     color: 1, 1, 1, 1
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

Test().run()