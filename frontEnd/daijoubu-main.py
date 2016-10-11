# IMPORTANT:
# Rename this py file to main.py before running
# daijoubu.kv is the accompanying kv file

import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty

# Screen class instances to be manipulated in the kv file
class ScreenDai(Screen):
    pass
class ScreenJou(Screen):
    pass
class ScreenBu(Screen):
    pass

# Creating the screen manager class
class Haruna(ScreenManager):
    # Unassigned objects that are linked to the screen classes in the kv file
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)

# Build the screen manager as an app
class DaijoubuApp(App):
    def build(self):
        return Haruna()

# Run the app
if __name__ == '__main__':
    DaijoubuApp().run()
