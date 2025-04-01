"""
     This function retrieves a list of all files in the given directory path.
     It filters out and collects only those files whose names start with "deep".
     The filtered list is then returned. If the directory is not found, an empty list is returned.

"""
import os


def thats_the_way(path: str) -> list:

    try:
        dir_list = os.listdir(path)
        file_list = []
        for file_name in dir_list:
            if file_name.startswith("deep"):
                file_list.append(file_name)
        return file_list
    except FileNotFoundError:
        print("Directory doesn't exist")
        return []


if __name__ == '__main__':
    print(thats_the_way(r"content/week05/images"))
    