class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not name or not isinstance(name, str):
            raise ValueError ("Please enter a Name")
        if not price > 0:
            raise ValueError ("Price can not be negative")
        if quantity < 0:
            raise ValueError ("Quantity cannot be negative")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity can not be less than 0 ")
        self.quantity = quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buys a given quantity of the product.
            Returns the total price (float) of the purchase.
            Updates the quantity of the product.
            In case of a problem (when? think about it), raises an Exception.
        """
        if quantity <= 0:
            raise ValueError ("Quantity to buy must be greater than 0")
        if quantity > self.quantity:
            raise ValueError ("Not enough quantity available")
        total_price = self.price * quantity
        new_quantity = self.quantity -quantity
        self.set_quantity(new_quantity)
        return total_price
