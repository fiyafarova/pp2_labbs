import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print("File deleted")
    else:
        print("File does not exist or is not accessible")

delete_file(r"/Users/sofiyasafarova/Desktop/2sem/pp2/lab_6/elements.txt")