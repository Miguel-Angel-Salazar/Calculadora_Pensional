from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class HelloApp(App):
    def build(self):
        self.contenedor = BoxLayout()
        self.contenedor.orientation = "vertical"

        self.nombre = TextInput(hint_text = "Ingrese su nombre")

        self.saludar = Button(text = "Saludar")
        self.saludar.bind(on_press = self.mostrar_saludo)

        self.saludo = Label(text = "Hello World",
                     color = (1, 0, 0, 1),
                     font_size = 40,
                     font_name = "Roboto-Italic")
        
        self.contenedor.add_widget(self.nombre)
        self.contenedor.add_widget(self.saludar)
        self.contenedor.add_widget(self.saludo)
        return self.contenedor
    
    def mostrar_saludo(self, sender):
        self.saludo.text = "Hola " + self.nombre.text


if __name__ == "__main__":
    HelloApp().run()