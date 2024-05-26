#я делала эти задания на паре практике но только спустя время поняла что пуш не сработал извините пожалуйста

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, restaurant_level):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.restaurant_level = restaurant_level

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, restaurant_level, restime, location):
        super().__init__(restaurant_name, cuisine_type, restaurant_level)
        self.restime = restime
        self.location = location
        self.flavors = ['Шоколадное', 'Пломбир', 'Клубничное']

    def flavors_restaurant(self):
        print('Список мороженого: ', IceCreamStand.flavors)

    def flavors_add(self):
        if 'Крем-брюле' not in self.flavors:
            self.flavors.append('Крем-брюле')
            print('Список мороженого: ', IceCreamStand.flavors)

    def flavors_rem(self):
        if 'Пломбир' in self.flavors:
            self.flavors.remove('Пломбир')
            print('Список мороженого: ', IceCreamStand.flavors)


IceCreamStand = IceCreamStand('Холодок', 'Мороженое', '5', '12', 'СПб')
IceCreamStand.flavors_restaurant()
IceCreamStand.flavors_rem()
IceCreamStand.flavors_add()