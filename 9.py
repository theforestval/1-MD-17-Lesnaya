import os
from PIL import Image, ImageFilter
import csv


def first():
    os.mkdir("fivee")
    photos = os.listdir("five")
    for i in photos:
        photo = Image.open(os.path.join("five", i))
        gray = photo.filter(ImageFilter.CONTOUR)
        gray.save(f"{"fivee"}/filter{i}")

def second():
    os.mkdir("fiveee")
    photos = os.listdir("five")
    for i in photos:
        split = os.path.splitext(i)
        if split[1] == ".jpg":
            photo = Image.open(os.path.join("five", i))
            gray = photo.filter(ImageFilter.CONTOUR)
            gray.save(f"{"fiveee"}/filter{i}")

def third():
    print('Нужно купить: ')
    products = [['Молоко', '2', '80'], ['Сыр', '1','500'], ['Хлеб', '2', '70']]
    sum = 0
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(products)
    with open('products.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, count, price = " ".join(row).split(" ")
            sum = sum + int(count)*int(price)
            print(f"{name} - {count} шт. за {price} руб.")
        print('Итоговая сумма: ', sum, 'руб.')

third()




