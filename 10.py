def first():
    import json
    products = [
        {
            "name": "Шоколад",
            "price": 50,
            "available": True,
            "weight": 100
        },
        {
            "name": "Кофе",
            "price": 100,
            "available": False,
            "weight": 250
        },
        {
            "name": "Чай",
            "price": 70,
            "available": True,
            "weight": 50
        }
    ]
    with open('products.json', 'w') as file:
        json.dump(products, file)
    with open('products.json', 'r') as json_file:
        products = json.load(json_file)
        for p in products:
            print('Название: ' + p["name"])
            print('Цена: ' + str(p["price"]))
            print('Вес: ' + str(p["weight"]))
            if p["available"] == True:
                print('В наличии!')
            else:
                print('Нет в наличии!')

def second():
    import json
    products = [
        {
            "name": "Шоколад",
            "price": 50,
            "available": True,
            "weight": 100
        },
        {
            "name": "Кофе",
            "price": 100,
            "available": False,
            "weight": 250
        },
        {
            "name": "Чай",
            "price": 70,
            "available": True,
            "weight": 50
        }
    ]
    with open('products.json', 'w') as file:
        json.dump(products, file)

    urname = input('Введите название продукта ')
    urprice = input('Введите цену продукта ')
    urweight = input('Введите вес продукта ')
    urravailable = (input('Продукт в наличии? '))
    if urravailable == "да":
        uravailable = True
    else:
        uravailable = False

    with open('products.json') as file:
        products = json.load(file)
        products.append({
            "name": urname,
            "price": urprice,
            "weight": urweight,
            "available": uravailable
         })
        with open('products.json', 'w') as file:
            json.dump(products, file)

    with open('products.json', 'r') as json_file:
        products = json.load(json_file)
        for p in products:
            print('Название: ' + p["name"])
            print('Цена: ' + str(p["price"]))
            print('Вес: ' + str(p["weight"]))
            if p["available"] == True:
                print('В наличии!')
            else:
                print('Нет в наличии!')

second()


