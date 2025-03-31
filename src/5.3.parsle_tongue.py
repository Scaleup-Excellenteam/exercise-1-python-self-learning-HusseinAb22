
def parsle_tongue():
    """
    Reads a binary file, decodes it as ASCII, and extracts lowercase words.

    Yields lowercase words that are at least 5 characters long and end with '!'.
    Non-lowercase sequences are ignored. If the file is missing, prints an error message.
    """

    try:
        with open(r"./logo.jpg", 'rb') as file:
            combined = file.read()
            text = combined.decode('ascii', errors='ignore')
            current = ""
            for char in text:
                if char.islower():
                    current += char
                elif char == '!':
                    if len(current) >= 5:
                        yield current
                    current = ""
                else:
                    current = ""
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':

    for line in parsle_tongue():
        print(line)