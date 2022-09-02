#Exercise 2
try:
    def make_shirt(size='large', message='John 3:16'):
        print("\nI'm going to make a " + size + " t-shirt.")
        print('It will say, "' + message + '"')

    make_shirt()
    make_shirt(size='medium')
    make_shirt('medium', 'PRAISE!.')

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')