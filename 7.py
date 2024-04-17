from PIL import Image
def first():
    image = Image.open('ежик.jpg')
    print(f"цветовая модель: {image.mode}")
    print(f"формат: {image.format}")
    print(f"размер: {image.size}")

def second():
    image = Image.open('ежик.jpg')
    img1 = image.reduce(3)
    img1.save('ежик1.jpg')
    img2 = image.transpose(Image.FLIP_LEFT_RIGHT)
    img2.save('ежик2.jpg')
    img3 = image.transpose(Image.FLIP_TOP_BOTTOM)
    img3.save('ежик3.jpg')

def third():
    image = Image.open('1.jpg')
    gray1 = image.convert('L')
    gray1.show()

third()












