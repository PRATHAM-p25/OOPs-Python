class Product:
    def _init_(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def _init_(self, product_name, price, brand, warranty):
        super()._init_(product_name, price)
        self.brand = brand
        self.warranty = warranty
 
    def display_electronic_product(self): 
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)


class MobilePhone(ElectronicProduct):
    def _init_(self, product_name, price, brand, warranty, ram, storage):
        super()._init_(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        print("RAM:", self.ram)
        print("Storage:", self.storage)


mobile = MobilePhone("iPhone 15", 80000, "Apple", "1 Year", "8GB", "256GB")

mobile.display_product()
mobile.display_electronic_product()
mobile.display_mobile_details()