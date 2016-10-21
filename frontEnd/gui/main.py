from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics import *
from kivy.properties import ObjectProperty, StringProperty

grid = GridLayout(cols=5, spacing=10, size_hint_y=None)
#box = BoxLayout(orientation='horizontal')
#anchor=AnchorLayout(anchor_x='right',anchor_y='top')
#anchor.size_hint = (.5,.5)
#with anchor.canvas:
#	anchor.anchor_x='right'
#	anchor.anchor_y='top'
#	Color(1.,0,0)
#	Rectangle(pos=(500,0),size=(100,100))

#lWelcome = Label(text="Welcome to Myx!", font_size=14)
#anchor.add_widget(lWelcome)
# Make sure the height is such that there is something to scroll.
#grid.bind(minimum_height=grid.setter('height'))
#for j in range(200):
#    btn = Button(text=str(j), size_hint_y=None, height=40)
#    grid.add_widget(btn)

#scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
#scroll.add_widget(grid)

#box.add_widget(anchor)
#box.add_widget(scroll)

class Myx(FloatLayout):
	label_wid=ObjectProperty()
	info = StringProperty()
	def do_action(self):
		self.label_wid.text ='bob'
		self.info = 'new bob'

class MyxApp(App):

	def build(self):
		return Myx(info='hello')

if __name__ == '__main__':
	MyxApp().run()
