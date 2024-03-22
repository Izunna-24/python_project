class Human:
    number_of_eyes = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def sleep(self):
        print(f"{self.name} sleeping ....")

    def eat(self):
        print("eating...")

#overides
    def __str__(self):
        return f"{self.name} is {self.gender}"


n1 = Human(6.1, 'male', 'pery')
n2 = Human(5.2, 'female', 'meschak')
n3 = Human(4.1, 'shemale', 'korede')

print(n1)
