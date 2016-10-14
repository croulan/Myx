from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

grid = GridLayout(cols=5, spacing=10, size_hint_y=None)
box = BoxLayout(orientation='horizontal')
anchor=AnchorLayout(anchor_x='right',anchor_y='top')

lWelcome = Label(text="Welcome to Myx!", font_size=14)
anchor.add_widget(lWelcome)
# Make sure the height is such that there is something to scroll.
grid.bind(minimum_height=grid.setter('height'))
for j in range(200):
    btn = Button(text=str(j), size_hint_y=None, height=40)
    grid.add_widget(btn)

scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
scroll.add_widget(grid)

box.add_widget(anchor)
box.add_widget(scroll)

runTouchApp(box)
