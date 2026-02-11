class Calculator:

    def __call__(self, a, b):
        return a + b


obj = Calculator()

print(obj(10, 20))
