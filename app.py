### Main Menu:
# 1. list of available items
#    i. print all the available items to the user
# 2. add a new item
#    i. ask for name, condition, price and qnt
# 3. swap an item
#     i. Search for item
#     ii. if found then they can swap
#     iii. rate the swap
# 4. delete an item
#     i. remove the item from database
import os

class Swapy:
    ### creating the constructor
    def __init__(self, db_path):
        self.db_path = db_path
        self.data = []
        self.read_data()

    def print_menu(self):
        print('----------Welcome to the Swapy------------')
        print('---------Main Menu-----------')
        print('1. Check the Catalogue')
        print('2. Add item into the catalogue')
        print('3. Remove an item from the catalogue')

    def read_data(self):
        if not os.path.exists(self.db_path):
            print('Path does not exist.')
            raise FileExistsError



## instanciation/ creating the object of class
swapy = Swapy('dat.txt')
swapy.print_menu()