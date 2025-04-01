"""
    This function takes two dates as input, converts them to epoch timestamps,
    generates a random timestamp between them, converts it back to a date,
    and checks if the resulting date falls on a Monday.
    If it does, it prints a specific message.
"""
import random as rnd
import datetime


def no_vinnigrete(input_date1, input_date2):
    """ changing the first  date to date format then epoch format"""
    date1 = datetime.datetime.strptime(input_date1, "%Y-%m-%d")
    epoch1 = int(date1.timestamp())
    """ changing the first  date to date format then epoch format"""
    date2 = datetime.datetime.strptime(input_date2, "%Y-%m-%d")
    epoch2 = int(date2.timestamp())
    if epoch1 < epoch2:
        random_epoch = rnd.randint(epoch1, epoch2)
    else:
        random_epoch = rnd.randint(epoch2, epoch1)
    random_date = datetime.datetime.fromtimestamp(random_epoch)
    if not random_date.weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")


if __name__ == '__main__':
    no_vinnigrete("2023-07-10", "2023-07-10")
