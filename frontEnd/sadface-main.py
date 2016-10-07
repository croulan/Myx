# IMPORTANT:
# Rename this py file to main.py before running
# Rename accompanying kv file to my.kv before running

import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class myApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    myApp().run()
