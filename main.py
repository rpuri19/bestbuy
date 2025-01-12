import products
from store import Store

def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products_in_store = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products_in_store[0], 1), (products_in_store[1], 2)]))


if __name__ == "__main__":
    main()