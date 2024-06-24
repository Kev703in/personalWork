class Person():
    def __init__(self):
        self.name = input("Enter your Name: ")

    def talk(self):
        print(f"you can talk {self.name}")


person = Person()
person.talk()