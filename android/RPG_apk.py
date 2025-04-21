import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import pyperclip as pc
import logic as lg

kivy.require('2.0.0')
class RPG(App):
    def build(self):
      return BoxLayout()
    def password_generator(self):
      input2= self.root.ids.input2.text
      input1= self.root.ids.input1.text
      #print("user inputs", input1, input2)
      password=lg.getInput(input1,input2)
      self.root.ids.output.text = password
      pc.copy(password)
      

          

if __name__ == "__main__":
  RPG().run()
