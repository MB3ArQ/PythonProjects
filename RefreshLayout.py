from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import ILeftBodyTouch, OneLineIconListItem
from kivymd.theming import ThemeManager
from kivymd.utils import asynckivy

Builder.load_string('''
<ItemForList>
    text: root.text
    IconLeftSampleWidget:
        icon: root.icon
<Example@MDFloatLayout>
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: app.title
            md_bg_color: 0, 1, 0, 1
            background_palette: 'Primary'
            elevation: 4
            left_action_items: [['menu', lambda x: x]]
        MDScrollViewRefreshLayout:
            id: refresh_layout
            refresh_callback: app.refresh_callback
            root_layout: root
            spinner_color: "brown"
            circle_color: "white"
            MDGridLayout:
                id: box
                adaptive_height: True
                cols: 1
''')

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

class ItemForList(OneLineIconListItem):
    icon = StringProperty()

class Example(MDApp):
    title = 'Example Refresh Layout'
    screen = None
    x = 0
    y = 15
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Orange"
        self.screen = Factory.Example()
        self.set_list()

        return self.screen
    
    def set_list(self):
        async def set_list():
            names_icons_list = list(md_icons.keys())[self.x:self.y]
            for name_icon in names_icons_list:
                await asynckivy.sleep(0)
                self.screen.ids.box.add_widget(ItemForList(icon=name_icon, text=name_icon))
        asynckivy.start(set_list())

    def refresh_callback(self, *args):
        def refresh_callback(interval):
            self.screen.ids.box.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list()
            self.screen.ids.refresh_layout.refresh_done()
            self.tick = 0
        Clock.schedule_once(refresh_callback, 1)

Example().run()