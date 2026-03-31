from kivy.app import App
from main import Questionnaire
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window

Window.clearcolor = "#ffffff"

class MyApp(App):
    def build(self):
        screen_manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Questionnaire())
        return screen_manager

app = MyApp()
app.run()