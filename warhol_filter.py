"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():
    image = SimpleImage.blank(WIDTH, HEIGHT)
    for a in range(N_ROWS):
        for i in range(N_COLS):
            for y in range(PATCH_SIZE):
                for x in range(PATCH_SIZE):
                    patch = make_recolored_patch()
                    pixel = patch.get_pixel(x, y)
                    image.set_pixel(x + (i*PATCH_SIZE), y + (a*PATCH_SIZE), pixel)
    image.show()

def make_recolored_patch():
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0
        pixel.blue = pixel.blue * 1.5
    return patch

if __name__ == '__main__':
    main()