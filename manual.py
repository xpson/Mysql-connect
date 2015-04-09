__author__ = 'Administrator'
print 'hello'
class FirstClass:
    def setdate(self,value):
        self.data=value
    def display(self):
        print(self.data)
x = FirstClass()
x.setdate('Kingarthur')
x.display()