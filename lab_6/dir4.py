import os

def count_lines(file_path):
    counter = 0
    with open(file_path, 'r') as file:
        for line in file:
            counter += 1
    return counter


print("Number of lines:", count_lines(r"/Users/sofiyasafarova/Desktop/2sem/pp2/lab_5/row.txt"))