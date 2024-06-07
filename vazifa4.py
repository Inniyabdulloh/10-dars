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


def gap_sana(txt_file):
    with open(txt_file, 'r') as f:
        result = ' '
        text = f.read().split('.')

        for gap in text:
            if len(gap) > len(result):
                result = gap
        return result


def create_protses_funksions()-> list:
    file_list = file_counter()
    protsesses = []
    for file in file_list:
        def my_protses():
            return f"{file} faylidagi eng uzun gap {gap_sana(file)} "

        task = Process(target=my_protses)
        task.run()
        protsesses.append(my_protses())

    return protsesses

# print(gap_sana("mytxt.txt"))
print(create_protses_funksions())