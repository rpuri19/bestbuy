import products
import store
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]

best_buy = store.Store(product_list)

def start(store):
    while True:
        print("Store Menu:")
        print("----------")
        print("1: List all products in store")
        print("2: Show total amount")
        print("3: Make an Order")
        print("4: Quit")

        user_input = input("Please choose a number: ")

        if user_input == "1":
            list_all_products()
        elif user_input == "2":
            show_total_amount()
        elif user_input =="3":
            make_an_order()
        elif user_input == "4":
            break
        else:
            print("Invalid Input")

def list_all_products():
    for items in best_buy.get_all_products():
        print(items)


def show_total_amount():
    number_of_items_in_store = best_buy.get_total_quantity()
    print (f"Total of {number_of_items_in_store} items in store.")


def make_an_order():
    products_in_store = best_buy.get_all_products()

    print(best_buy.order([(products_in_store[0], 1), (products_in_store[1], 2)]))


if __name__ == "__main__":
    start(best_buy)
