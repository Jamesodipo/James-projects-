from kivymd.app import MDApp
from kivy.lang import Builder
class MyApp(MDApp):
	def build(self):
		self.theme_cls.theme_style="Dark"
		self.theme_cls.primary_palette = "BlueGray"
		return Builder.load_file("login.kv")
	def logger(self):
		self.root.ids.welcome_label.text=f"Hello {self.root.ids.user.text}\n"
	def clear(self):
		self.root.ids.welcome_label.text="WELCOME"
		self.root.ids.user.text=""
		self.root.ids.password.text=""
		
MyApp().run()