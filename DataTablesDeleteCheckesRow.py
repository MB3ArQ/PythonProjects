from kivy.metrics import dp
from kivy.lang import Builder
from kivy.clock import Clock

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen

KV = '''
MDBoxLayout:
    orientation: "vertical"
    padding: "56dp"
    spacing: "24dp"
    MDData:
        id: table_screen
    MDRaisedButton:
        text: "DELETE CHECKED ROWS"
        on_release: table_screen.delete_checked_rows()
'''

class MDData(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = [
            ["1", "Asep Sudrajat", "Male", "Soccer"],
            ["2", "Egy", "Male", "Soccer"],
            ["3", "Tanos", "Demon", "Soccer"],
        ]
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("No", dp(30)),
                ("No Urut", dp(30)),
                ("Alamat Pengirim", dp(30)),
                ("No Surat", dp(60))
            ]
        )
        self.data_tables.row_data = self.data
        self.add_widget(self.data_tables)
    
    def delete_checked_rows(self):
        def deselecet_rows(*args):
            self.data_tables.table_data.select_all("normal")
        for data in self.data_tables.get_row_checks():
            self.data_tables.remove_row(data)
        Clock.schedule_once(deselecet_rows)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

MyApp().run()