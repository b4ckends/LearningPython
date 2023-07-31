def run():
    def converter(country, value):
        pesos = int(input(f'\nEnter the amount of {country.capitalize()} pesos: '))
        usd = pesos / value 
        print(f'\nYou have a total of ${usd:.2f} dollars')
        

    menu = int(input(f"""\
Welcome to the converter of pesos to dollars

            1.Mexican Pesos
            2.Colombian Pesos
            3.Argentian Pesos

Choose an option: """))
    if menu == 1:
        converter('Mexican', 19.85)
    elif menu == 2:
        converter('Colombian', 585.45)
    elif menu == 3:
        converter('argentian', 239.56)

if __name__ == '__main__':
    run()