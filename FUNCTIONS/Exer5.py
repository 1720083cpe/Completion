#Exercise 5
try:
    def show_celebrity(celebrities):
        for celebrity in celebrities:
            print(celebrity.title())

    celebrities = ['Vhong Navarro', 'Daniel Padilla', 'James Reid']
    show_celebrity(celebrities)

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')