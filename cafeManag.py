menu={
  'Pizza':40,
  'Pasta':50,
  'Burger':60,
  'Salad':70,
  'Coffee':80
}

def item_dealer(order_total=0):
  
  item_1=input('Enter the item you want to Order: ')
  if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order!")
  else:
    print(f"Your orderd item {item_1} is not available yet!")

  another_item=input("Do you want to add another Item (Yes/No)?: ")
  if another_item.strip().lower()=="yes":
    item_dealer(order_total)
  else:
    print(f'The total amount of items to pay is: {order_total} Rs')

print("Welcome  in Our Resturant")
for item in menu:
  print(f"{item}: Rs{menu[item]}")

item_dealer()


