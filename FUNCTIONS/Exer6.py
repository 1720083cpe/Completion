#Exercise 6
try:
    def show_celebrities(celebrities):
        for celebrity in celebrities:
            print(celebrity)

    def make_great(celebrities):
        great_celebrities= []

        while celebrities:
            celebrity = celebrities.pop()
            great_celebrity = celebrity + ' Too Good to be True'
            great_celebrities.append(great_celebrity)

        for great_celebrity in great_celebrities:
            celebrities.append(great_celebrity)

    celebrities = ['Kathyrn Bernardo', 'Daniel Padilla', 'Yves Flores']
    show_celebrities(celebrities)

    print("\n")
    make_great(celebrities)
    show_celebrities(celebrities)

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')