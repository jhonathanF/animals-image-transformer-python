ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", ".",  "=", "."]

def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel//25]
    return ascii_str

def to_greyscale(image):
    return image.convert("L")

def resize(image, new_width = 80):
    old_width, old_height = image.size
    new_height = new_width * old_height / old_width
    return image.resize((new_width, math.ceil(new_height)))

imgUrl = requests.get('https://shibe.online/api/shibes').json()[0]

imgContent = requests.get(imgUrl).content
img = Image.open(BytesIO(imgContent))

# buff = BytesIO()
# img.save(buff, format="JPEG")
# img_str = base64.b64encode(buff.getvalue())
# print( img_str)

#resize image
img = resize(img);
#convert image to greyscale image
greyscale_image = to_greyscale(img)
# convert greyscale image to ascii characters
ascii_str = pixel_to_ascii(greyscale_image)
img_width = greyscale_image.width
ascii_str_len = len(ascii_str)
ascii_img=""
#Split the string based on width  of the image
for i in range(0, ascii_str_len, img_width):
    ascii_img += ascii_str[i:i+img_width] + "\n"
    
with open("ascii_image.txt", "w") as f:
    f.write(ascii_img)

print(ascii_img)

var = input()