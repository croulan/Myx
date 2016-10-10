from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.base import runTouchApp

# create a dropdown with 10 buttons

#class BobScreen(GridLayout):
#	def __init__(self,**kwargs):
#		super(BobScreen,self).__init__(**kwargs)
#		self.add_widget(Label(text='wowowow'))
#		self.add_widget(mainbutton)

#dropdown = DropDown()
#for index in range(10):

    # when adding widgets, we need to specify the height manually (disabling
    # the size_hint_y) so the dropdown can calculate the area it needs.

#    btn = Button(text='Value %d' % index, size_hint_y=None, height=44)

    # for each button, attach a callback that will call the select() method
    # on the dropdown. We'll pass the text of the button as the data of the
    # selection.
#    btn.bind(on_release=lambda btn: dropdown.select(btn.text))

    # then add the button inside the dropdown
#    dropdown.add_widget(btn)

# create a big main button
#mainbutton = Button(text='bob', size_hint=(None, None),center_x=500,center_y=500)

#buttonBob = Button(text='Cotton Eye Joe',font_size=14)

# show the dropdown menu when the main button is released
# note: all the bind() calls pass the instance of the caller (here, the
# mainbutton instance) as the first argument of the callback (here,
# dropdown.open.).

#mainbutton.bind(on_release=dropdown.open)

# one last thing, listen for the selection in the dropdown list and
# assign the data to the button text.
#dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))



class MyApp(App):
	def build(self):
		return MyxApp();

if __name__== '__main__':
	MyApp().run()
