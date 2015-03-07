
class Person(object):
	def __init__(self, name, gender, birth):
	   self.name = name
	   self.gender = gender
	   self.birth = birth
	

class Person2(object):
	def __init__(self, name):
	   self.name = name
	   self.__gender__ = 'gender'
	   self.__birth = 'birth'

xiaoming = Person('ming', 'male', '1991-1-1')
xiaoming2 = Person2('ming')


print xiaoming2.gender
