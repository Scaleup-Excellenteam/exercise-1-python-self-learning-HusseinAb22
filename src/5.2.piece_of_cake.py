def piece_of_cake(prices, optionals=[], **bought_items):
    """
    Calculates the total cost of bought items, excluding optional ones.

    - `prices`: dict of item prices per 100g
    - `optionals`: list of items to exclude
    - `**bought_items`: items and their quantities in grams

    Returns the total cost as an integer.
    """
    checkout = 0
    for item, price in bought_items.items():
        if item not in optionals and item in bought_items:
            checkout += int((price/100) * prices[item])
    return checkout


if __name__ == '__main__':
    print(piece_of_cake(
            prices={'milk': 20, 'chocolate': 18},
            optionals=['milk'],
            milk=200,
            chocolate=100
        ))