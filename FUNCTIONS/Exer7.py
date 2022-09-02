#Exercise 7
try:
    def make_milktea(*items):
        print("\nI'll make you a great milktea:")
        for item in items:
            print("  ...adding " + item + " to your milktea.")
        print("Your milktea is ready!")

    make_milktea('sago', 'ice', 'syrup')
    make_milktea('buko pandan', 'taro', 'okinawa')
    make_milktea('winter melon')

except:
    print('Error!.')
finally:
    print('\nThank you for using this program')