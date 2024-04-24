def first():
    from PIL import Image
    alyona = Image.open('alyona.jpg')
    crop = alyona.crop((300, 50, 900, 700))
    crop.show()
    crop.save('alyona_crop.jpg')

def second():
    from PIL import Image
    dict = {"новый год": "новыйгод.jpg", "восьмое марта": "8марта.jpg" }
    holiday = input("Открытка к какому празднику вам нужна? ")
    if holiday in dict:
        card = Image.open(dict[holiday])
        card.show()
    else:
        print("Открытка к данному празднику не найдена")


def third():
    from PIL import Image, ImageDraw, ImageFont
    alyona = Image.open('alyona.jpg')
    crop = alyona.crop((300, 50, 900, 700))
    name = input("Введите имя человека, которого хотите поздравить ")
    font = ImageFont.truetype("arial.ttf", 30)
    draww = ImageDraw.Draw(crop)
    draww.text((270, 550), name, font=font, fill='purple')
    draww.text((240, 600), "поздравляю!", font=font, fill='pink')
    crop.save("new_crop.jpg")
    crop.show()

third()






