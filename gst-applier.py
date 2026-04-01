price = float(input("Enter product price: "))
category = input("Enter category (electronics/food items/stationary/medical): ")

if category == "electronics":
    gst = 18
elif category == "food items":
    gst = 8
elif category == "stationary":
    gst = 10        
elif category == "medical":
    gst = 5
else:
    gst = 12

total_price = price + (price * gst // 100)

print("GST applied:", gst, "%")
print("Total price:", total_price)