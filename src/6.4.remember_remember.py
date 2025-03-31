import cv2
import numpy as np


def remember_remember(img):
    """
    Reads an image and scans its pixels to extract a hidden message.

    - Converts the image into a NumPy array.
    - Checks each pixel column-wise for a specific RGB pattern: (1, 1, 1).
    - For each match, adds the corresponding ASCII character (based on the row index) to a sentence.

    Returns:
    - str: The decoded message built from matching pixels.
    """
    img = cv2.imread(img)
    matrix = np.array(img)
    height, width = matrix.shape[:2]
    sentence = ""
    for i in range(width):
        for j in range(height):

            if matrix[j][i][0] == 1 and matrix[j][i][1] == 1 and matrix[j][i][2] == 1:
                sentence += chr(j)
                break
    return sentence


if __name__ == '__main__':
    print(remember_remember(r"code.png"))
