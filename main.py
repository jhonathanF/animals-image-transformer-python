import requests
import base64
from io import BytesIO
from PIL import Image

imgUrl = requests.get('https://shibe.online/api/shibes').json()[0]

imgContent = requests.get(imgUrl).content
img = Image.open(BytesIO(imgContent))
buff = BytesIO()
img.save(buff, format="JPEG")
img_str = base64.b64encode(buff.getvalue())
print(img_str)