def add_to_cart(item_name, price, *args, **kwargs):
  """
  Function adds an item to the shopping cart.

  Function arguments:
    item_name: The name of the item.
    price: The price of the item.
    *args: list of discounts (percentages).
    **kwargs: Keyword arguments for item details.

  Function output returns :
    The final price of the item after applying discounts.
  """
  final_price = price
  for discount in args:
    final_price -= (discount / 100) * final_price
  return final_price

cart = {}
total_cost = 0

while True:
  item_name = input("Enter item name (or 'done' to finish): ")
  if item_name.lower() == 'done':
    break

  price = float(input("Enter item price: "))

  discount_input = input("Enter discounts (if any, separated by spaces): ")

  # handling the discount
  discounts = []
  if discount_input:
      discounts = [float(d) for d in discount_input.split()]


  item_details = input("Enter item details (e.g., color=red size=large): ")

  final_price = add_to_cart(item_name, price, *discounts)

  if item_name in cart:
    print(f"{item_name} already exists in the cart.")
  else:
    cart[item_name] = {"price": final_price, "details": item_details}
    total_cost += final_price
    print(f"Item added: {item_name} - Final Price: ${final_price:.2f}")

print("\n--- Cart Summary ---")
for i, (item, details) in enumerate(cart.items(), 1):
  print(f"{i}. {item.capitalize()} - ${details['price']:.2f} ({details['details']})")

print(f"Total Cost: ${total_cost:.2f}")
