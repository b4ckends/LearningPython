def start():
    menu = int(input(f"""
Welcome to the menu of infinite tables

        1.Unique
        2.Infinite

Choose an option to start: """))

    if menu == 1:
        number = int(input(f'\nEnter a positive number: '))
        if number > 1:
           n = 1
           print(f'\nTABLE OF {number}')
           while n < 10:
            print(f'{n} x {number} = {n*number}')
            n += 1


if __name__ == '__main__':
    start()
