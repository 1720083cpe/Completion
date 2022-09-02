filename = 'guest_book.csv'

with open(filename) as f:
    contents = f.read()
    print(contents)