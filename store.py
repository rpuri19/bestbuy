import products

class Store:
    def __init__(self, all_products = None):
        self.all_products = all_products if all_products is not None else []

    def add_product(self, product):
        self.all_products.append(product)

    def remove_product(self, product):
        if product in self.all_products:
            self.all_products.remove(product)
        else:
            raise ValueError ("Product Not in List")

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.all_products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        return self.all_products

    def order(self, shopping_list):
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0

        for product, quantity in shopping_list:
            if product not in self.all_products:
                print ("Product not in list")
                continue
            if not product.is_active():
                print ("Product not available.")
                continue
            if product.get_quantity() < quantity:
                print("Insufficient stock.")
                continue
            total_price += product.buy(quantity)
        return total_price

"""
bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)
store = Store([bose, mac])
print (store.get_all_products())
price = store.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")
"""