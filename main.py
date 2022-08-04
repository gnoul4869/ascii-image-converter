import re
from PIL import Image

# These characters are ordered based on the surface they occupy when they are rendered.
# The character “`" uses the least surface on the screen, while the character “$” is having the biggest area.
ASCII_CHARACTERS_BY_SURFACE = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# White pixel will be represented as (255, 255, 255).
# Maximum brightness will be 765 (255 + 255 + 255)
MAX_PIXEL_BRIGHTNESS = 255 * 3

# response = requests.get(
#     'https://media.discordapp.net/attachments/988299242315591700/988504645175492628/sf_vi.jpg?width=1618&height=910')


def convert_pixel_to_ascii_char(px):
    (r, g, b) = px
    pixel_brightness = r + g + b
    brightness_weight = len(ASCII_CHARACTERS_BY_SURFACE) / MAX_PIXEL_BRIGHTNESS
    char_index = int(pixel_brightness * brightness_weight) - 1
    return ASCII_CHARACTERS_BY_SURFACE[char_index]


def convert_image_to_ascii(img):
    (imgWidth, imgHeight) = img.size

    ascii_art = []

    for y in range(0, imgHeight - 1):
        line = ''
        for x in range(0, imgWidth - 1):
            px = img.getpixel((x, y))
            line += convert_pixel_to_ascii_char(px)
        ascii_art.append(line)

    print('Converted image to ascii art successfully!')
    return ascii_art


def save_ascii_art_to_file(ascii_art, filename):
    with open(filename, 'w') as f:
        for line in ascii_art:
            f.write(line + '\n')

    print(f'file saved as {filename}')


def main():
    img = Image.open('image.jpg')

    # url = 'https://media.discordapp.net/attachments/928115805789499412/1004711472737304587/copycat.jpg'
    # img = Image.open(requests.get(url, stream=True).raw)

    filename = re.sub(r'(\.\w+)$', '', img.filename)

    if not filename:
        filename = 'ascii_art'

    ascii_art = convert_image_to_ascii(img)
    save_ascii_art_to_file(ascii_art, f'{filename}.txt')


if __name__ == '__main__':
    main()
