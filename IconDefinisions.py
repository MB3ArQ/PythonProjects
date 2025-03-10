from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem
from kivy.graphics.context_instructions import Color

Builder.load_string(
'''
#:import images_path kivymd.images_path
<CustomOneLineIconListItem>
    IconLeftWidget:
        icon: root.icon
<PreviousMDIcons>
    canvas.before:
        Color:
            rgba: .576, .141, .314, .57
        Rectangle:
            pos: self.pos
            size: self.size
    MDBoxLayout:
        orientation: 'vertical'
        spancing: dp(10)
        padding: dp(20)
        MDBoxLayout:
            adaptive_height: True
            MDIconButton:
                icon: 'magnify'        
            MDTextField:
                id: search_field
                hint_text: 'Search Icon'
                color_mode: 'custom'
                on_text: root.set_list_md_icons(self.text, True)
                line_color_focus: 1, 1, .533, 1
                mode: 'round'
                fill_color: .34, 1, .03, 1

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'
            RecycleBoxLayout:
                padding: dp(10)
                default_size: None, dp(48)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
)

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()

class PreviousMDIcons(Screen):
    def set_list_md_icons(self, text="", search=False):
        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": name_icon,
                    "text": name_icon,
                    "callback": lambda x: x
                }
            )
        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon:
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()

MainApp().run()