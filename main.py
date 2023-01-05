import os
import json
path1 = r'productList.json'
path2 = r'totalList.json'


def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == 'admin' and password == '1234':
        print("logged successfully")
        administrator_menu()
    else:
        print("Incorrect Username or Password.")
        print("Please Try Again!")
        menu()


def menu():
    print("----------------------------------------------")
    print("               SUPERMARKET MENU               ")
    print("----------------------------------------------")
    print("[1] Administrator                             ")
    print("[2] Customer                                  ")
    print("[3] Exit                                      ")
    print("----------------------------------------------")
    choice()


def choice():
    user_input_choice = int(input("Please Enter You Choice : "))
    if user_input_choice == 1:
        login()
    elif user_input_choice == 2:
        customer_menu()
    elif user_input_choice == 3:
        exit()
    else:
        print("Wrong Choice! Please Try Again.")
        menu()


def administrator_menu():
    print("----------------------------------------------")
    print("              ADMINISTRATOR MENU              ")
    print("----------------------------------------------")
    print("[1] Add Product                               ")
    print("[2] Edit Product                              ")
    print("[3] Delete Product                            ")
    print("[4] Back                                      ")
    print("----------------------------------------------")
    choice_administrator = int(input("Please Enter Your Choice : "))
    if choice_administrator == 1:
        add_product()
    elif choice_administrator == 2:
        edit_product()
    elif choice_administrator == 3:
        delete_product()
    elif choice_administrator == 4:
        menu()
    else:
        print("Wrong Choice! Please Try Again.")
        menu()


def customer_menu():
    print("----------------------------------------------")
    print("                CUSTOMER MENU                 ")
    print("----------------------------------------------")
    print("[1] Buy Product                               ")
    print("[2] Back                                      ")
    print("[3] Exit                                      ")
    print("----------------------------------------------")
    choice_customer = int(input("Please Enter Your Choice : "))
    if choice_customer == 1:
        buy_product()
    elif choice_customer == 2:
        menu()
    elif choice_customer == 3:
        exit()
    else:
        print("Wrong Choice! Please Try Again.")
        menu()


def add_product():
    print("----------------------------------------------")
    print("               ADD PRODUCT MENU               ")
    print("----------------------------------------------")
    product_dict = {'name': [], 'quantity': [], 'price': []}
    product_list = list(product_dict.values())
    product_name_list = product_list[0]
    product_quantity_list = product_list[1]
    product_price_list = product_list[2]

    if os.path.isfile(path1):
        with open('productList.json') as productList_file:
            product_dict = json.load(productList_file)

            product_list = list(product_dict.values())
            product_name_list = product_list[0]
            product_quantity_list = product_list[1]
            product_price_list = product_list[2]

            print("----------------------------------------------")
            print("               ADD PRODUCT MENU               ")
            print("----------------------------------------------")
            for i in range(len(product_name_list)):
                print([i + 1], "NAME:", product_name_list[i],
                      "QUANTITY:", product_quantity_list[i],
                      "PRICE:", product_price_list[i], "THB")
                print("----------------------------------------------")
            try:
                product_name = input("Please Enter Name of Product : ").capitalize()
                product_quantity = int(input("Please Enter Quantity of Product : "))
                product_price = int(input("Please Enter Price of Product : "))
            except ValueError:
                print("Please Enter Again!")
                administrator_menu()

            # checks if product name already in list
            if product_name in product_name_list:
                # find the index of product_name_list
                index = product_name_list.index(product_name)
                # remove old quantity
                product_quantity_list.remove(product_quantity_list[index])
                # remove old price
                product_price_list.remove(product_price_list[index])
                # insert new quantity
                product_quantity_list.insert(index, product_quantity)
                # insert new price
                product_price_list.insert(index, product_price)

                with open('productList.json', mode='w', encoding='utf8') as productList_file_w:
                    productList_file_w.write(json.dumps(product_dict, indent=2))

                with open('productList.json') as productList_file_r:
                    product_dict = json.load(productList_file_r)

                    product_list = list(product_dict.values())
                    product_name_list = product_list[0]
                    product_quantity_list = product_list[1]
                    product_price_list = product_list[2]

                    print("----------------------------------------------")
                    print("               ADD PRODUCT MENU               ")
                    print("----------------------------------------------")
                    for i in range(len(product_name_list)):
                        print([i + 1], "NAME:", product_name_list[i],
                              "QUANTITY:", product_quantity_list[i],
                              "PRICE:", product_price_list[i], "THB")
                        print("----------------------------------------------")

            else:
                product_name_list.append(product_name)
                product_quantity_list.append(product_quantity)
                product_price_list.append(product_price)

                with open('productList.json', mode='w', encoding='utf8') as productList_file_w:
                    productList_file_w.write(json.dumps(product_dict, indent=2))

                with open('productList.json') as productList_file_r:
                    product_dict = json.load(productList_file_r)

                    product_list = list(product_dict.values())
                    product_name_list = product_list[0]
                    product_quantity_list = product_list[1]
                    product_price_list = product_list[2]

                    print("----------------------------------------------")
                    print("               ADD PRODUCT MENU               ")
                    print("----------------------------------------------")
                    for i in range(len(product_name_list)):
                        print([i + 1], "NAME:", product_name_list[i],
                              "QUANTITY:", product_quantity_list[i],
                              "PRICE:", product_price_list[i], "THB")
                        print("----------------------------------------------")

    else:
        product_name = input("Please Enter Name of Product : ").capitalize()
        product_quantity = int(input("Please Enter Quantity of Product : "))
        product_price = int(input("Please Enter Price of Product : "))

        product_name_list.append(product_name)
        product_quantity_list.append(product_quantity)
        product_price_list.append(product_price)
        for i in range(len(product_name_list)):
            print(product_name_list[i], product_quantity_list[i], product_price_list[i])

        print("That doesn't exists. I will Create!")
        with open('productList.json', mode='w', encoding='utf8') as productList_file:
            productList_file.write(json.dumps(product_dict, indent=2))

        with open('productList.json') as productList_file:
            product_dict = json.load(productList_file)

            product_list = list(product_dict.values())
            product_name_list = product_list[0]
            product_quantity_list = product_list[1]
            product_price_list = product_list[2]

            print("----------------------------------------------")
            print("               ADD PRODUCT MENU               ")
            print("----------------------------------------------")
            for i in range(len(product_name_list)):
                print([i + 1], "NAME:", product_name_list[i],
                      "QUANTITY:", product_quantity_list[i],
                      "PRICE:", product_price_list[i], "THB")
                print("----------------------------------------------")

    choice_add_product = input("Do you want to add product more ? (y/n) : ")
    if choice_add_product == 'Y' or choice_add_product == 'y':
        add_product()
    elif choice_add_product == 'N' or choice_add_product == 'n':
        administrator_menu()
    else:
        print("Wrong Choice!")
        menu()


def edit_product():
    print("----------------------------------------------")
    print("               EDIT PRODUCT MENU              ")
    print("----------------------------------------------")
    if os.path.isfile(path1):
        with open('productList.json') as productList_file:
            product_dict = json.load(productList_file)

            product_list = list(product_dict.values())
            product_name_list = product_list[0]
            product_quantity_list = product_list[1]
            product_price_list = product_list[2]

            print("----------------------------------------------")
            print("               EDIT PRODUCT MENU              ")
            print("----------------------------------------------")
            for i in range(len(product_name_list)):
                print([i + 1], "NAME:", product_name_list[i],
                      "QUANTITY:", product_quantity_list[i],
                      "PRICE:", product_price_list[i], "THB")
                print("----------------------------------------------")

            product_name = input("Please Enter Name of Product : ")
            if product_name in product_name_list:
                index = product_name_list.index(product_name)
                product_name_list.remove(product_name_list[index])
                product_quantity_list.remove(product_quantity_list[index])
                product_price_list.remove(product_price_list[index])

                product_name = input("Please Enter New Name of Product : ")
                product_quantity = int(input("Please Enter New Quantity of Product : "))
                product_price = int(input("Please Enter New Price of Product : "))

                product_name_list.append(product_name)
                product_quantity_list.append(product_quantity)
                product_price_list.append(product_price)

                with open('productList.json', mode='w', encoding='utf8') as productList_file_w:
                    productList_file_w.write(json.dumps(product_dict, indent=2))

                with open('productList.json') as productList_file_r:
                    product_dict = json.load(productList_file_r)

                    product_list = list(product_dict.values())
                    product_name_list = product_list[0]
                    product_quantity_list = product_list[1]
                    product_price_list = product_list[2]

                    print("----------------------------------------------")
                    print("               EDIT PRODUCT MENU              ")
                    print("----------------------------------------------")
                    for i in range(len(product_name_list)):
                        print([i + 1], "NAME:", product_name_list[i],
                              "QUANTITY:", product_quantity_list[i],
                              "PRICE:", product_price_list[i])
                        print("----------------------------------------------")

                choice_edit_product = input("Do you want to edit product more ? (y/n) : ")
                if choice_edit_product == 'y' or choice_edit_product == 'Y':
                    edit_product()
                elif choice_edit_product == 'N' or choice_edit_product == 'n':
                    administrator_menu()
                else:
                    print("Wrong Choice")
                    menu()

            elif product_name not in product_name_list:
                print(product_name, "don't have in productList file.")
                administrator_menu()
    else:
        print("You don't have the product in productList file.")
        administrator_menu()


def delete_product():
    print("----------------------------------------------")
    print("              DELETE PRODUCT MENU             ")
    print("----------------------------------------------")
    if os.path.isfile(path1):
        with open('productList.json') as productList_file:
            product_dict = json.load(productList_file)

            product_list = list(product_dict.values())
            product_name_list = product_list[0]
            product_quantity_list = product_list[1]
            product_price_list = product_list[2]

            print("----------------------------------------------")
            print("              DELETE PRODUCT MENU             ")
            print("----------------------------------------------")
            for i in range(len(product_name_list)):
                print([i + 1], "NAME:", product_name_list[i],
                      "QUANTITY:", product_quantity_list[i],
                      "PRICE:", product_price_list[i], "THB")
                print("----------------------------------------------")

            product_name = input("Please Enter Name of Product : ")
            if product_name in product_name_list:
                index = product_name_list.index(product_name)
                product_name_list.remove(product_name_list[index])
                product_quantity_list.remove(product_quantity_list[index])
                product_price_list.remove(product_price_list[index])

                with open('productList.json', mode='w', encoding='utf8') as productList_file_w:
                    productList_file_w.write(json.dumps(product_dict, indent=2))

                with open('productList.json') as productList_file_r:
                    product_dict = json.load(productList_file_r)

                    product_list = list(product_dict.values())
                    product_name_list = product_list[0]
                    product_quantity_list = product_list[1]
                    product_price_list = product_list[2]

                    print("----------------------------------------------")
                    print("              DELETE PRODUCT MENU             ")
                    print("----------------------------------------------")
                    for i in range(len(product_name_list)):
                        print([i + 1], "NAME:", product_name_list[i],
                              "QUANTITY:", product_quantity_list[i],
                              "PRICE:", product_price_list[i], "THB")
                        print("----------------------------------------------")

                choice_edit_product = input("Do you want to edit product more ? (y/n) : ")
                if choice_edit_product == 'y' or choice_edit_product == 'Y':
                    edit_product()
                elif choice_edit_product == 'N' or choice_edit_product == 'n':
                    administrator_menu()
                else:
                    print("Wrong Choice")
                    menu()
            elif product_name not in product_name_list:
                print(product_name, "don't have in productList file.")
                administrator_menu()
    else:
        print("You don't have the product in productList file.")
        administrator_menu()


def total():
    sum_price = 0
    with open('totalList.json') as total_file:
        total_dict = json.load(total_file)

        total_list = list(total_dict.values())
        total_price_list = total_list[2]

        for price in total_price_list:
            sum_price = sum_price + price
    print("----------------------------------------------")
    print("Total                                ", sum_price, "THB")
    print("----------------------------------------------")


def sum_list(name, amount, price):
    total_dict = {'name': [], 'quantity': [], 'price': []}
    total_list = list(total_dict.values())
    total_name_list = total_list[0]
    total_quantity_list = total_list[1]
    total_price_list = total_list[2]

    if os.path.isfile(path2):
        with open('totalList.json') as total_file:
            total_dict = json.load(total_file)

            total_list = list(total_dict.values())
            total_name_list = total_list[0]
            total_quantity_list = total_list[1]
            total_price_list = total_list[2]

            if name in total_name_list:
                print("Duplicate")
                # find the index of product_name_list
                index = total_name_list.index(name)

                # insert new quantity
                total_quantity_list.insert(index+1, amount+total_quantity_list[index])
                # insert new price
                total_price_list.insert(index+1, price+total_price_list[index])

                # remove old quantity
                total_quantity_list.remove(total_quantity_list[index])
                # remove old price
                total_price_list.remove(total_price_list[index])

                with open('totalList.json', mode='w', encoding='utf8') as f:
                    f.write(json.dumps(total_dict, indent=2))
            else:
                total_name_list.append(name)
                total_quantity_list.append(amount)
                total_price_list.append(price)
                for i in range(len(total_name_list)):
                    print(total_name_list[i], "x", total_quantity_list[i], "=", total_price_list[i], "THB")

                with open('totalList.json', mode='w', encoding='utf8') as total_file_w:
                    total_file_w.write(json.dumps(total_dict, indent=2))
    else:
        total_name_list.append(name)
        total_quantity_list.append(amount)
        total_price_list.append(price)

        print("That doesn't exists. I will Create!")
        with open('totalList.json', mode='w', encoding='utf8') as total_file:
            total_file.write(json.dumps(total_dict, indent=2))


def sum_list_clear():
    with open('totalList.json') as total_file:
        total_dict = json.load(total_file)

        total_list = list(total_dict.values())
        total_name_list = total_list[0]
        total_quantity_list = total_list[1]
        total_price_list = total_list[2]

        total_name_list.clear()
        total_quantity_list.clear()
        total_price_list.clear()
        with open('totalList.json', mode='w', encoding='utf8') as file:
            file.write(json.dumps(total_dict, indent=2))


def print_receipt():
    with open("totalList.json") as total_file:
        total_dict = json.load(total_file)

        total_list = list(total_dict.values())
        total_name_list = total_list[0]
        total_quantity_list = total_list[1]
        total_price_list = total_list[2]
        print("----------------------------------------------")
        print("                   RECEIPT                    ")
        print("----------------------------------------------")
        for x in range(len(total_name_list)):
            print(total_name_list[x], "x", total_quantity_list[x], "=", total_price_list[x], "THB")
        total()


def buy_product():
    print("----------------------------------------------")
    print("                BUY PRODUCT MENU              ")
    print("----------------------------------------------")

    if os.path.isfile(path1):
        with open('productList.json') as productList_file:
            product_dict = json.load(productList_file)

            product_list = list(product_dict.values())
            product_name_list = product_list[0]
            product_quantity_list = product_list[1]
            product_price_list = product_list[2]

            for i in range(len(product_name_list)):
                print([i+1], "NAME:", product_name_list[i],
                      "QUANTITY:", product_quantity_list[i],
                      "PRICE:", product_price_list[i], "THB")
        print("----------------------------------------------")
        product_name = input("What do you want to buy ? (name of product) : ").capitalize()
        product_amount = int(input("Please Enter Amount of Product : "))

        if product_name in product_name_list:
            index = product_name_list.index(product_name)

            # Quantity
            if product_quantity_list[i] < product_amount:
                print("There are not enough products.")
                print("Please Enter Again.")
                buy_product()
            elif product_quantity_list[i] > product_amount:
                product_quantity_left = product_quantity_list[index] - product_amount
                product_quantity_list.insert(index + 1, product_quantity_left)
                product_quantity_list.remove(product_quantity_list[index])
            else:
                print("Please Enter Again.")
                buy_product()

            # Price
            product_price = product_price_list[index] * product_amount
            product_price_list.insert(index+1, product_price_list[index])
            product_price_list.remove(product_price_list[index])

            # Name
            product_name_list.insert(index+1, product_name_list[index])
            product_name_list.remove(product_name_list[index])

            with open('productList.json', mode='w', encoding='utf8') as productList_file_w:
                productList_file_w.write(json.dumps(product_dict, indent=2))

            sum_list(product_name, product_amount, product_price)
            choice_buy_product = input("Do you want to buy more ? (y/n) : ")
            if choice_buy_product == 'Y' or choice_buy_product == 'y':
                buy_product()
            elif choice_buy_product == 'N' or choice_buy_product == 'n':
                print_receipt()
            else:
                print("Wrong Choice!")
                customer_menu()
        elif product_name not in product_name_list:
            print(product_name, "don't have in store.")
            customer_menu()

    else:
        print("You don't have the product in store.")
        menu()
    sum_list_clear()


menu()
