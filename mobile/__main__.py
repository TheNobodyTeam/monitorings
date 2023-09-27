
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        label = Label(text="Bonjour, Kivy !", font_size=24)
        layout.add_widget(label)
            
        button = Button(text="Cliquez-moi !")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):

        self.root.clear_widgets()  #
        new_label = Label(text="Bouton cliqué !", font_size=24)
        self.root.add_widget(new_label)

if __name__ == '__main__':
    MyApp().run()
