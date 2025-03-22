from kivy.app import App
from kivy.uix.label import Label


class HelloApp(App):
    def build(self):
        return Label(text = "Hello World",
                     color = (1, 0, 0, 1),
                     font_size = 40,
                     font_name = "Roboto-Italic")


if __name__ == "__main__":
    HelloApp().run()