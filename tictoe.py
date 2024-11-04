from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.app import App
Builder.load_file("tictoe.kv")
class FloatLayout(Widget):
	turn = "x"
	winner = False
	x_win =0
	O_win = 0
	def no_winner(self):
		if self.winner ==  False and \
			self.ids.btn1.disabled==True and \
			self.ids.btn2.disabled==True and \
			self.ids.btn3.disabled==True and \
			self.ids.btn4.disabled==True and \
			self.ids.btn5.disabled==True and \
			self.ids.btn6.disabled==True and \
			self.ids.btn7.disabled==True and \
			self.ids.btn8.disabled==True and \
			self.ids.btn9.disabled==True:
				self.ids.scores.text = "ITS A TIE ■■■■"
	def end_game(self,a,b,c):
		self.winner=True
		a.color="red"
		b.color="red"
		c.color="red"
		
		self.disable_all_the_buttons()
		self.ids.scores.text = f'{a.text} wins !'
		if a.text=="x":
			self.x_win = self.x_win +1
		else:
			self.O_win = self.O_win +1
			
		self.ids.game.text = f'x_wins: {self.x_win} | Os_wins: {self.O_win}'
		
	def disable_all_the_buttons(self):
		self.ids.btn1.disabled=True
		self.ids.btn2.disabled=True
		self.ids.btn3.disabled=True
		self.ids.btn4.disabled=True
		self.ids.btn5.disabled=True
		self.ids.btn6.disabled=True
		self.ids.btn7.disabled=True
		self.ids.btn8.disabled=True
		self.ids.btn9.disabled=True
		
		
	def win(self):
		
		
		#Across
		if self.ids.btn1.text != ""  and self.ids.btn1.text==self.ids.btn2.text and self.ids.btn2.text == self.ids.btn3.text:
			self.end_game(self.ids.btn1,self.ids.btn2,self.ids.btn3)
			
			
			
			
			
		if self.ids.btn4.text != ""  and self.ids.btn4.text==self.ids.btn5.text and self.ids.btn5.text == self.ids.btn6.text:
			self.end_game(self.ids.btn4,self.ids.btn5,self.ids.btn6)
			
			
			
			
			
		if self.ids.btn7.text != ""  and self.ids.btn7.text==self.ids.btn8.text and self.ids.btn8.text == self.ids.btn9.text:
			self.end_game(self.ids.btn7,self.ids.btn8,self.ids.btn9)
			
			
			#Down
		if self.ids.btn1.text != ""  and self.ids.btn1.text==self.ids.btn4.text and self.ids.btn4.text == self.ids.btn7.text:
			self.end_game(self.ids.btn1,self.ids.btn4,self.ids.btn7)
			
		if self.ids.btn2.text != ""  and self.ids.btn2.text==self.ids.btn5.text and self.ids.btn5.text == self.ids.btn8.text:
			self.end_game(self.ids.btn2,self.ids.btn5,self.ids.btn8)
			
			
		if self.ids.btn3.text != ""  and self.ids.btn3.text==self.ids.btn6.text and self.ids.btn6.text == self.ids.btn9.text:
			self.end_game(self.ids.btn3,self.ids.btn6,self.ids.btn9)
		#digonally
		if self.ids.btn1.text != ""  and self.ids.btn1.text==self.ids.btn5.text and self.ids.btn5.text == self.ids.btn9.text:
			self.end_game(self.ids.btn1,self.ids.btn5,self.ids.btn9)
			
		if self.ids.btn3.text != ""  and self.ids.btn3.text==self.ids.btn5.text and self.ids.btn5.text == self.ids.btn7.text:
			self.end_game(self.ids.btn3,self.ids.btn5,self.ids.btn7)
			
		self.no_winner()
	
			
	def presser(self,btn):
		if self.turn =="x" :
			btn.text = "x"
			btn.disabled= True
			self.ids.scores.text = "O's turn!"
			self.turn = "O"
		else:
			btn.text = "O"
			btn.disabled= True
			self.ids.scores.text = "x's turn!"
			self.turn = "x"
		self.win()
			
	def restart(self):
		self.turn="x"
		
		self.ids.btn1.disabled=False
		self.ids.btn2.disabled=False
		self.ids.btn3.disabled=False
		self.ids.btn4.disabled=False
		self.ids.btn5.disabled=False
		self.ids.btn6.disabled=False
		self.ids.btn7.disabled=False
		self.ids.btn8.disabled=False
		self.ids.btn9.disabled=False
		
		self.ids.btn1.text= ""
		self.ids.btn2.text= ""
		self.ids.btn3.text= ""
		self.ids.btn4.text= ""
		self.ids.btn5.text= ""
		self.ids.btn6.text= ""
		self.ids.btn7.text= ""
		self.ids.btn8.text= ""
		self.ids.btn9.text= ""
		
		self.ids.btn1.color= "blue"
		self.ids.btn2.color= "blue"
		self.ids.btn3.color= "blue"
		self.ids.btn4.color= "blue"
		self.ids.btn5.color= "blue"
		self.ids.btn6.color= "blue"
		self.ids.btn7.color= "blue"
		self.ids.btn8.color= "blue"
		self.ids.btn9.color= "blue"
		
		self.ids.scores.text = "x's goes first "
		
		self.winner = False
	
class TicToeApp(App):
	def build (self):
		return FloatLayout()
		
	
if __name__ =="__main__":		
	TicToeApp().run()