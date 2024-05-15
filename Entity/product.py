class Product:
    def __init__(self,productId,productName,description,price,quantityInStock ,type):
        self.productId=productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type

    def get_productId(self):
        return self.productId

    def set_productId(self, productId):
        self.productId = productId

    def get_productName(self):
        return self.productName

    def set_productName(self, productName):
        self.productName = productName

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantityInStock(self):
        return self.quantityInStock

    def set_quantityInStock(self, quantityInStock):
        self.quantityInStock = quantityInStock

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_warrantyPeriod(self):
        return self.warrantyPeriod

    def set_warrantyPeriod(self, warrantyPeriod):
        self.warrantyPeriod = warrantyPeriod

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, type, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, type)
        self.size = size
        self.color = color

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color