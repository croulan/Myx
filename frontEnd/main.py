from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class MyxGui(Widget):
	pass

class MyxApp(App):
	def build(self):
		return MyxGui();

if __name__== '__main__':
	MyxApp().run()
