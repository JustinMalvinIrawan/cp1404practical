from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculation(self):
        number = self.get_validated_miles()
        convert_kilometer = MILES_TO_KM * number
        self.root.ids.output_label.text = str(convert_kilometer)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesToKmApp().run()