class Person:
  def __init__(self,name, age):
    self.name = name
    self.age = age

  def introduce(self, to_name):
    print("안녕" + to_name + "! 내 이름은 " + self.name + "이고 나이는 " + str(self.age) + "이야.")

class Police(Person):
  def arrest(self, to_arrest):
    print("넌 체포다" + to_arrest)

class Programer(Person):
  def program(self, to_program):
    print("이거 만들어야지 " + to_program)

me = Person("다윤", 21)
jungwoo = Police("정우", 24)
doyoung = Programer("도영", 26)

doyoung.introduce("다윤")
jungwoo.arrest("다윤")

doyoung.program("웹서비스")