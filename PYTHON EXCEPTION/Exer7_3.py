try:
     locations = ['Palawan', 'Boracay', 'Nasugbu', 'Calatagan', 'Laiya']

     print("Original order:")
     print(locations)

     print("\nReversed:")
     locations.reverse()
     print(locations)

     print("\nOriginal order:")
     locations.reverse()
     print(locations)

     print("\nAlphabetical")
     locations.sort()
     print(locations)

     print("\nReverse alphabetical")
     locations.sort(reverse=True)
     print(locations)
  
except:
    print('error')

finally:
    print('thank you for visiting!')