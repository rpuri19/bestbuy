import products
import store

def menu_display():
    menu = {
        1: "List all products in store",
        2: "Show total amount",
        3: "Make an Order",
        4: "Quit"
    }
    print("Store Menu:")
    print("----------")
    for key, value in menu.items():
        print(f"{key} : {value}")


def start():

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = store.Store(product_list)

    while True:
        menu_display()
        user_input = input("Please choose a number: ")

        if user_input == "1":
            list_all_products(best_buy)
        elif user_input == "2":
            show_total_amount(best_buy)
        elif user_input =="3":
            make_an_order(best_buy)
        elif user_input == "4":
            break
        else:
            print("Invalid Input")

def list_all_products(best_buy):
    for items in best_buy.get_all_products():
        print(items)


def show_total_amount(best_buy):
    number_of_items_in_store = best_buy.get_total_quantity()
    print (f"Total of {number_of_items_in_store} items in store.")


def order_inputs():
    inputs_from_user = []
    print("When you want to finish order, enter empty text.")
    while True:
        input_1 = input("Which product # do you want? ")
        if not input_1:
            break
        input_2 = input("What amount do you want? ")
        if not input_2:
            break
        if not input_2.isdigit():
            print("Error adding product")
            continue

        inputs_from_user.append((int(input_1), int(input_2)))

    return inputs_from_user

def make_an_order(best_buy):
    tuples_for_orderid_and_number = order_inputs()
    try:
        total_price = best_buy.order(tuples_for_orderid_and_number)
        print(f"\nAmount to be paid: {total_price}\n")
    except ValueError:
        print("Error accepting order. Please retry.")



if __name__ == "__main__":
    start()
