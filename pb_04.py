# addition of two numbers using inheritance

class one:
    def input(self):
        self.first = int(input("Enter first number : "))
        self.second = int(input("Enter second number : "))

class Third(one):
    def add(self):
        super().input()
        self.addition = self.first + self.second
        print("Sum is:", self.addition)

obj = Third()
obj.add()