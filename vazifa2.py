import os
from multiprocessing import Process


def file_counter()-> list: # funksiya joylashgan papkadagi barcha txt filelarni list typeda qaytaruvchi funksiya
    path = os.getcwd()
    files = os.listdir(path)
    txt_files = []
    for file in files:
        if file.endswith(".txt"):
            txt_files.append(file)
    return txt_files


def son_sana(txt_file):
    with open(txt_file, 'r') as f:
        result = 0
        text = f.read()
        for char in text:
            try:
                char = int(char)
                result += 1
            except:
                continue
        return result


def create_protses_funksions()-> list:
    file_list = file_counter()
    protsesses = []
    for file in file_list:
        def my_protses():
            return f"{file} faylida {son_sana(file)} son bor"

        task = Process(target=my_protses)
        task.run()
        protsesses.append(my_protses())

    return protsesses


print(create_protses_funksions())