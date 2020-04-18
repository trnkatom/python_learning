class Product:
    _price = 0.0
    tax_rate = 0.12

    def __init__(self, base_price):
        self._price = base_price

    # creates new property returning base price enhanced with tax
    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    # sets _price to new value (= overriding base_price) from which the property "price" calculates _price with tax
    @price.setter
    def price(self, new_price):
        self._price = new_price

product = Product(10)
print("_price = {} --> price = {}".format(product._price, product.price))
product.price = 20
print("_price = {} --> price = {}".format(product._price, product.price))