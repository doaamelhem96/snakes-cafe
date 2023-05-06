Resturants_Menu = [
    {"category": "Appetizers", "items": ["Wings", "Cookies", "Spring Rolls"]},
    {"category": "Entrees", "items": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]},
    {"category": "Desserts", "items": ["Ice Cream", "Cake", "Pie"]},
    {"category": "Drinks", "items": ["Coffee", "Tea", "Unicorn Tears"]}
]

def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
''')

def cafe_list():
    for category in Resturants_Menu:
        print(f'\n {category["category"]} \n {"----"}')
        print("\n".join(category["items"]))

def user_insertion():
    print('''
    ***********************************
    What would you like to order?
    ***********************************
    ''')



orders = {}
def main():
  
    user_input = ""
    while user_input.lower() != "quit":
        user_input = input(">").lower()  
        if user_input in [item.lower() for category in Resturants_Menu for item in category["items"]]:
            if user_input not in orders:
                orders[user_input] = 1
                print(orders[user_input], "order of", user_input, "has been added to your meal")
            else:
                orders[user_input] += 1
                print(orders[user_input], "orders of", user_input, "has been added to your meal")
        elif user_input != "quit":
            print('''****************
            *** Sorry, that item does not exist. ***
            *** Please choose another item from the Snakes Cafe menu. ***
            ***************************''')
    total_orders = sum(orders.values())
    print("Total orders:", total_orders)

def end_application():
    print("Here is your order summary:")
    for item, count in orders.items():
              print(count, "order of", item)
    print("Thanks for using the Snakes Cafe application!")
if __name__ == "__main__": 
    intro()  
    cafe_list()
    user_insertion()
    main()
    end_application()

