import requests
import base64
from io import BytesIO
from PIL import Image

def toBase64(img):
    buff = BytesIO()
    img.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    print(img_str)

def printHr():
    print('---------------------------------------------------')

def main():
    printHr()
    print('|  Olá, digite para continuar:                    |')
    print('|                                                 |')
    print('|  1 - Base64                                     |')
    print('|  2 - Save To File                               |')
    printHr()
    option = input()
    print('Gerando...')
    imgUrl = requests.get('https://shibe.online/api/shibes').json()[0]
    imgContent = requests.get(imgUrl).content
    img = Image.open(BytesIO(imgContent))
    
    if(option == '1'):
        return toBase64(img)
    if(option == '2'):
        img.save("test.png", "png")

main()