class Test:
	x=123#static
	def __init__(self):
		self.y=111#instance
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=777#access static
t1.y=666#access instance
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)