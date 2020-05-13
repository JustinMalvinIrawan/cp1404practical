from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabels(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.name_to_phone:
            temp_label = Label(text=name, id=name)
            temp_label.bind(on_press=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_label)

    def press_entry(self, instance):
        name = instance.id
        self.status_text = "{}'s number is {}".format(name, self.name_to_phone[name])

    def clear_all(self):
        self.root.ids.entries_box.clear_widgets()


DynamicLabels().run()