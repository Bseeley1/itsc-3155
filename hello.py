userInput = input("Original price: ")
price = float(userInput)

if (price >= 10) :
   discountedPrice = price - 3.14
else :
   discountedPrice = price - 1         

print("Discounted price: %.2f\n" % discountedPrice)