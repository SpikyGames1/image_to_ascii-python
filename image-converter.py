import sys
import argparse
from PIL import Image

def png_to_ascii(image_path, width):

    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    aspect_ratio = img.height / img.width
    new_width = width
    new_height = int(aspect_ratio * new_width * 0.55)

    resample_method = getattr(Image, 'LANCZOS')
    img = img.resize((new_width, new_height), resample_method)

    img = img.convert('RGBA')

    for y in range(new_height):
        for x in range(new_width):
            r, g, b, a = img.getpixel((x, y))
            color = f"\033[48;2;{r};{g};{b}m"
            print(f"{color}#\033[0m", end='')
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path")
    parser.add_argument("-w", "--width", type=int, default=120)
    args = parser.parse_args()

    png_to_ascii(args.image_path, args.width)
