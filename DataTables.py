from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

#https://kivymd.readthedocs.io/en/latest/components/datatables/

class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        box = MDBoxLayout(
            pos_hint={'center_x': .5},
            adaptive_size = True,
            padding = "24dp",
            spacing = "24dp",
        )

        for button_text in ["Add row", "Remove row"]:
            box.add_widget(
                MDRaisedButton(
                    text=button_text, on_release=self.on_button_press
                )
            )

        self.data_tables = MDDataTable(
            use_pagination = True,
            check = True,
            rows_num = 30,            
            background_color_header = "fc6d65",
            background_color_cell = "f7c1be",
            background_color_selected_cell = "bd0f06",
            column_data = 
            [
                ("No.", dp(30)),
                ("Status", dp(30), self.sort_on_team),
                ("[color=#32a838]Signal Name[/color]", dp(60), self.sort_on_signal),
                ("Severity", dp(30)),
                ("[color=#658dfc]Stage[/color]", dp(30)),
                ("Schedule", dp(30), self.sort_on_schedule),
                ("Team Lead", dp(30), self.sort_on_team)
            ],
            row_data = 
            [
                (
                    "1",
                    ("alert", [255/256, 165/256, 0, 1], "No Signal"),
                    "Astrid: NE shared managed",
                    "Medium",
                    "Triaged",
                    "0:33",
                    "Chase Nguyen"
                ),
                (
                    "2",
                    ("alert-circle", [1, 0, 0, 1], "Offline"),
                    "Cosmo: prod shared ares",
                    "Huge",
                    "Triaged",
                    "0:39",
                    "Brie Furman"
                ),
                (
                    "3",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Phoenix: prod shared lyra-lists",
                    "Minor",
                    "Not Triaged",
                    "3:12",
                    "Jeremy Lake"
                ),
                (
                    "4",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Sirius: NW prod shared locations",
                    "Negligible",
                    "Triaged",
                    "13:18",
                    "Angelica Howards"
                ),
                (
                    "5",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma"
                ),
                (
                    "5",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma"
                ),                
                (
                    "5",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma"
                ),
                (
                    "5",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma"
                ),
                (
                    "5",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma"
                ),
                (
                    "5",
                    ("checkbox-marked-circle", [39/256, 174/256, 96/256, 1], "Online"),
                    "Sirius: prod independent account",
                    "Negligible",
                    "Triaged",
                    "22:06",
                    "Diane Okuma"
                )
            ],
            sorted_on = 'Schedule',
            sorted_order = "ASC",
        )
        self.data_tables.bind(on_row_press = self.on_row_press)
        self.data_tables.bind(on_check_press = self.on_check_press)
        screen = MDScreen()
        screen.add_widget(self.data_tables)
        screen.add_widget(box)
        return screen

    def on_row_press(self, instanse_table, instanse_row):
        print(instanse_table, instanse_row)

    def on_check_press(self, instanse_table, instanse_row):
        print(instanse_table, instanse_row)

    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        return zip(
                *sorted(
                    enumerate(data), key = lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1])
                    ]
                    )
                )
            )
    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key = lambda l: l[1][-1]))

    def on_button_press(self, instanse_button: MDRaisedButton) -> None:
        try:
            {
                "Add row": self.add_row,
                "Remove row": self.remove_row
            }[instanse_button.text]()
        except KeyError:
            pass
    
    def add_row(self) -> None:
        last_num_row = int(self.data_tables.row_data[-1][0])
        self.data_tables.add_row((str(last_num_row + 1), None, None, None, None, None))
    
    def remove_row(self) -> None:
        if len(self.data_tables.row_data) > 1:
            self.data_tables.remove_row(self.data_tables.row_data[-1])

Example().run()