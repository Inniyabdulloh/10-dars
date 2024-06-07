import os
import string
from multiprocessing import Process


def file_counter()-> list: # funksiya joylashgan papkadagi barcha txt filelarni list typeda qaytaruvchi funksiya
    path = os.getcwd()
    files = os.listdir(path)
    txt_files = []
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files


def del_punktuations(txt_file):
    with open(txt_file, 'r') as f:
        text = f.read()
        result_text = ''
        for char in text:
            if char not in string.punctuation:
                result_text += char

        return result_text


def create_protses_funksions()-> list:
    file_list = file_counter()
    protsesses = []
    for file in file_list:
        def my_protses():
            return f"{del_punktuations(file)}"

        task = Process(target=my_protses)
        task.run()
        protsesses.append(my_protses())

    return protsesses


print(create_protses_funksions())