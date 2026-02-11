class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Mobile):
            return self.brand == other.brand and self.model == other.model
        return False


m1 = Mobile("Apple", "iPhone 15", 80000)
m2 = Mobile("Apple", "iPhone 15", 85000)
m3 = Mobile("Samsung", "S23", 75000)

print(m1 == m2)   
print(m1 == m3)  
print(m2 == m3)   
