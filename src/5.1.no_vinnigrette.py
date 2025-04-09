"""
This module contains a function that generates a random date between two input dates
and prints a message if the random date does not fall on a Monday.
"""

import random as rnd
import datetime


def no_vinnigrete():
    """
    Generates a random date between two given dates and checks if it falls on a Monday.
    Prints:
        A message if the generated random date is not a Monday.
    """
    while True:
        try:
            input_date1 = input("Enter the first date (YYYY-MM-DD): ")
            input_date2 = input("Enter the second date (YYYY-MM-DD): ")
            date1 = datetime.datetime.strptime(input_date1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(input_date2, "%Y-%m-%d")
            break  
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.\n")
    epoch1 = int(date1.timestamp())
    epoch2 = int(date2.timestamp())
    if epoch1 > epoch2:
        epoch1, epoch2 = epoch2, epoch1
    random_epoch = rnd.randint(epoch1, epoch2)
    random_date = datetime.datetime.fromtimestamp(random_epoch)
    if random_date.weekday() != 0:
        print("Ain't gettin' no vinaigrette today :(")


if __name__ == '__main__':
    no_vinnigrete()
