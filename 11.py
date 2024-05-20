class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, restaurant_level):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_level = restaurant_level
    def describe_restaurant(self):
        print('Ресторан ' + self.restaurant_name + ' и его ' + self.cuisine_type + ' кухня' )

    def open_restaurant(self):
        print('Ресторан открыт!')

    def changelevel_restaurant(self, newlevel):
        self.restaurant_level = newlevel

newRestaurant = Restaurant('Chang','азиатская', '5')
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

first_rest = Restaurant('Mimino', 'грузинская','5')
first_rest.describe_restaurant()

second_rest = Restaurant('Medici','итальянская','4')
second_rest.describe_restaurant()

third_rest = Restaurant('DuNord','французская','5')
third_rest.describe_restaurant()


