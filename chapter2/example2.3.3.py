class Peter:
	x = 3
	@property
	def buy(self):
		return self.x
	@buy.setter
	def buy(self, value):
		self.x = value
	
peter=Peter()
# print(peter.buy())
print(peter.buy)
peter.buy=5
print(peter.buy)