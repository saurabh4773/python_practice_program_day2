# subtraction of two numbers using inheritance

class one:
    def input(self):
        self.first = int(input("Enter first number : "))
        self.second = int(input("Enter second number : "))

class Third(one):
    def add(self):
        super().input()
        self.subtract = self.first - self.second
        print("Subtraction is:", self.subtract)

obj = Third()
obj.add()