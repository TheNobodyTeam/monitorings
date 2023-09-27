# Importer les modules Kivy nécessaires
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Classe principale de l'application
class MyApp(App):
    def build(self):
        # Crée une mise en page de boîte verticale
        layout = BoxLayout(orientation='vertical', padding=10)

        # Ajoute une étiquette de texte à la mise en page
        label = Label(text="Bonjour, Kivy !", font_size=24)
        layout.add_widget(label)

        # Ajoute un bouton à la mise en page
        button = Button(text="Cliquez-moi !")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Répond à l'événement de clic du bouton
        self.root.clear_widgets()  # Efface tous les widgets de la mise en page
        new_label = Label(text="Bouton cliqué !", font_size=24)
        self.root.add_widget(new_label)

# Point d'entrée de l'application
if __name__ == '__main__':
    MyApp().run()
