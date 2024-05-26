#я делала эти задания на паре практике но только спустя время поняла что пуш не сработал извините пожалуйста

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, restaurant_level):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_level = restaurant_level

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, restaurant_level, restime, location, flavours = []):
        super().__init__(restaurant_name, cuisine_type, restaurant_level)
        self.restime = restime
        self.location = location
        self.flavors = flavours

    def flavors_restaurant(self):
        print('Список мороженого: ', IceCreamStand.flavors)

    def flavors_add(self):
        pass


IceCreamStand = IceCreamStand('Холодок', 'Мороженое', '5', '12', 'СПб', ['Крем-брюле', 'Шоколадное', 'Пломбир'])
IceCreamStand.flavors_restaurant()