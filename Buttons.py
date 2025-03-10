from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton
KV = '''
MDScreen:
    md_bg_color: "#c1c9c2"
    MDIconButton:
        icon: "album"
        theme_icon_color: "Custom"
        icon_size: "64sp"
        icon_color: [.2, .34, .8, 1]
        md_bg_color: [.3, .1, .6, 1]
        pos_hint: {"center_x": .03, "center_y": .95}
    MDBoxLayout:
        id: box
        spacing: "56dp"
        adaptive_size: True
        pos_hint: {"center_x": .09, "center_y": .825}
    MDRaisedButton:
        text: "MDRaisedButton"
        md_bg_color: "green"
        pos_hint: {"center_x": .05, "center_y": .725}
    MDRectangleFlatButton:
        text: "MDRectangleFlatButton"
        theme_text_color: "Custom"
        text_color: "blue"
        line_color: "orange"
        pos_hint: {"center_x": .06, "center_y": .665}
    MDRectangleFlatIconButton:
        icon: "asterisk"
        text: "MDRectangleFlatIconButton"
        theme_text_color: "Custom"
        text_color: "white"
        line_color: "yellow"
        theme_icon_color: "Custom"
        icon_color: "red"
        pos_hint: {"center_x": .07, "center_y": .605}
    MDRectangleFlatIconButton:
        icon: "asterisk"
        text: "MDRectangleFlatIconButton"
        theme_text_color: "Custom"
        line_color: [0, 0, 0, 0]
        text_color: "white"
        theme_icon_color: "Custom"
        icon_color: "red"
        pos_hint: {"center_x": .07, "center_y": .545}
    MDRoundFlatButton:
        text: "MDRoundFlatButton"
        text_color: "white"
        line_color: "purple"
        line_width: 1.5
        pos_hint: {"center_x": .06, "center_y": .485}
    MDRoundFlatIconButton:
        text: "MDRoundFlatIconButton"
        icon: "car-wash"
        icon_color: "brown"
        text_color: "white"
        line_width: 1.5
        pos_hint: {"center_x": .065, "center_y": .425}
    MDFillRoundFlatButton:
        text: "MDFillRoundFlatButton"
        md_bg_color: [.639, .941, .655, 1]
        pos_hint: {"center_x": .065, "center_y": .365}
    MDFillRoundFlatIconButton:
        icon: "alert-plus"
        text: "MDFillRoundFlatIconButton"
        md_bg_color: [.71, .82, .075, 1]
        pos_hint: {"center_x": .07, "center_y": .305}
    MDTextButton:
        text: "MDTextButton"
        custom_color: "white"
        pos_hint: {"center_x": .07, "center_y": .245}
    MDFloatingActionButtonSpeedDial:
        icon: "format-letter-case"
        data: app.data
        root_button_anim: True
        hint_animation: True
        label_text_color: "black"
        label_bg_color: "orange"
        right_pad: True
        right_pad_value: "10dp"
        bg_color_root_button: "green"
        bg_color_stack_button: "blue"
        color_icon_stack_button: "white"
        color_icon_root_button: self.color_icon_stack_button
        bg_hint_color: "purple"
'''


class Example(MDApp):
    data = {
        'Alpha': 'alpha',
        'Betta': 'beta',
        'Gamma': 'gamma',
        'Epsilon': 'epsilon'
    }
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.material_style = "M3"
        return Builder.load_string(KV)
    def on_start(self):
        data = {
            "large": {"md_bg_color": "#3f9649", "text_color": "#9c9695"},
            "standard": {"md_bg_color": "#bf6460", "text_color": "#9c9695"},
            "small": {"md_bg_color": "#6e3f96", "text_color": "#9c9695"}
        }
        for type_button in data.keys():
            self.root.ids.box.add_widget(
                MDFloatingActionButton(
                    icon = "arrow-down-bold-hexagon-outline",
                    type = type_button,
                    theme_icon_color = "Custom",
                    md_bg_color = data[type_button]["md_bg_color"],
                    icon_color = data[type_button]["text_color"]
                )
            )
Example().run()