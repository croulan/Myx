# # IMPORTANT:
# Rename this py file to main.py before running

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

Builder.load_file('boxDesu.kv')
Builder.load_file('boxDesuwa.kv')
Builder.load_file('boxDesuka.kv')

class GridBuild(GridLayout):
    pass

class uluApp(App):
    def build(self):
        self.x = 100
        self.y = 100
        return GridBuild()

if __name__ == '__main__':
    uluApp().run()
