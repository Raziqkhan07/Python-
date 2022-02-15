class Person:
    name="Person"
    def speak(self):
        print( "Hi! Im %s"%self.name)

class Dad(Person):
     name = "Dad"

class Mom(Person):
     name = "Mom"

class Child(Person):
     name = "a Child"
     age  = 5
     def speak(self):
        print ("Hewwo, I am a %d year old child!"%self.age)

d = Dad()
m = Mom()
c = Child()

c.speak()
m.speak()
d.speak()