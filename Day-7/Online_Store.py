class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent

    def get_discounted_price(self):
        discount = (self.discount_percent / 100) * self.price
        return self.price - discount
    
p1=DiscountedProduct("laptop",1000,20)
print(p1.get_discounted_price())