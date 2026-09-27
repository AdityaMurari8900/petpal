from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

class PetPalPrototype(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        title_label = Label(text="PetPal Assistant (Prototype)", font_size='22sp', size_hint=(1, 0.15))
        layout.add_widget(title_label)
        
        self.species_label = Label(text="Select Pet Species:", size_hint=(1, 0.1))
        layout.add_widget(self.species_label)
        
        self.spinner = Spinner(text='Dog', values=('Dog', 'Cat', 'Bird'), size_hint=(1, 0.15))
        layout.add_widget(self.spinner)
        
        self.status_label = Label(text="Daily Care: Feed & Walk pending.", font_size='16sp', size_hint=(1, 0.2))
        layout.add_widget(self.status_label)
        
        action_btn = Button(text="Mark Daily Care Done", size_hint=(1, 0.2), background_color=(0.1, 0.6, 0.4, 1))
        action_btn.bind(on_press=self.mark_completed)
        layout.add_widget(action_btn)
        
        return layout

    def mark_completed(self, instance):
        selected_species = self.spinner.text
        self.status_label.text = f"Status: {selected_species} care completed for today!"

if __name__ == '__main__':
    PetPalPrototype().run()
