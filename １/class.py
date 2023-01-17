class Student:

  def __init__(self, name): #constructor
    self.name = name #attribute
  def avg(self, math, english): # method
    print((math + english) / 2)


a001 = Student("sato") # a001 = instance, Student() = class
print(a001.name)

a002 = Student("tanaka")
print(a002.name)


