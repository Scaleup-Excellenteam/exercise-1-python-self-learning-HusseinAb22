"""
Reads an image and scans its pixels to extract a hidden message.

- Converts the image into a NumPy array.
- Checks each pixel column-wise for a specific RGB pattern: (1, 1, 1).
- For each match, adds the corresponding ASCII character (based on the row index) to a sentence.

Returns:
- str: The decoded message built from matching pixels.
"""


from PIL import Image


def remember_remember(img_path):
    img = Image.open(img_path).convert("RGB")
    width, height = img.size
    pixels = img.load()

    sentence = ""
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if (r, g, b) == (1, 1, 1):
                sentence += chr(y)
                break
    return sentence


if __name__ == '__main__':
    print(remember_remember("code.png"))
