from modules.restaurant import Restaurant

restaurant = Restaurant('Olive Garden', 'Italian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()