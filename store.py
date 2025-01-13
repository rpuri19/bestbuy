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
        for i in range(len(self.all_products)):
            product = self.all_products[i]
            print(f"{i+1}: {product.name}, Price = {product.price}, Quantity = {product.quantity}")



    def order(self, shopping_list):
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0

        for product_id, quantity in shopping_list:
            if product_id > len(self.all_products):
                return "Not all product # entered valid. Please check "
            else:
                product = self.all_products[product_id - 1]

            if product not in self.all_products:
                return "Product not in list"
            if not product.is_active():
                return "Product not available."
            if product.get_quantity() < quantity:
                return "Insufficient stock."
            total_price += product.buy(quantity)
        return total_price