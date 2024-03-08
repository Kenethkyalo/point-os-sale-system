class Product:

  def __init__(self, product_ID, name, quantity_in_stock):
    self.product_ID = product_ID
    self.name = name
    self.quantity_in_stock = quantity_in_stock

  def calculate_value(self):
    raise NotImplementedError("Subclass must implement this method")


class ElectronicsProduct(Product):

  def __init__(self, product_ID, name, quantity_in_stock, price):
    super().__init__(product_ID, name, quantity_in_stock)
    self.price = price

  def calculate_value(self):
    return self.price * self.quantity_in_stock


class ClothingProduct(Product):

  def __init__(self, product_ID, name, quantity_in_stock, price_per_unit,
               size):
    super().__init__(product_ID, name, quantity_in_stock)
    self.price_per_unit = price_per_unit
    self.size = size

  def calculate_value(self):
    return self.price_per_unit * self.quantity_in_stock

  electronics_product = ElectronicsProduct(1, "Smartphone", 10, 500)
  #clothing_product = ClothingProduct(2, "Shirt", 20, 15, "M")

  print(electronics_product.calculate_value())
  #print(clothing_product.calculate_value())


class SimpleProduct(Product):

  def __init__(self, product_ID, name, quantity_in_stock, unit_price):
    super().__init__(product_ID, name, quantity_in_stock)
    self.unit_price = unit_price

  def calculate_value(self):
    return self.unit_price * self.quantity_in_stock


class PerishableProduct():

  def __init__(self, product_ID, name, quantity_in_stock, unit_price,
               expiry_date, shelf_life, datetime):

    def calculate_value(self):
      today = datetime.date.today()
      remaining_shelf_life = (self.shelf_life - (today - self.shelf_life)).days
      discount = 0
      if remaining_shelf_life < 7:
        discount = 0.1
      elif remaining_shelf_life < 14:
        discount = 0.05
      total_value = self.quantity_in_stock * self.unit_price * (1 - discount)
      return total_value


class DigitaProduct(Product):

  def __init__(self, product_ID, name, quantity_in_stock, price):

    def calculate_value(self):
      return self.price * self.quantity_in_stock
