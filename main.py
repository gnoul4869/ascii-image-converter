import requests
from PIL import Image

# These characters are ordered based on the surface they occupy when they are rendered.
# The character “`" uses the least surface on the screen, while the character “$” is having the biggest area.
ASCII_CHARACTERS_BY_SURFACE = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# White pixel will be represented as (255, 255, 255).
# Maximum brightness will be 765 (255 + 255 + 255)
MAX_PIXEL_BRIGHTNESS = 255 * 3

# response = requests.get(
#     'https://media.discordapp.net/attachments/988299242315591700/988504645175492628/sf_vi.jpg?width=1618&height=910')

img = Image.open('ff_xv_02.jpg')
(imgWidth, imgHeight) = img.size
