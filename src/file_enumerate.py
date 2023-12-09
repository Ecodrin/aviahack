import os
import shutil


def enumerate():
    path = '../data_wage'
    os.mkdir("../upgrate_data_wage")
    for root, d_names, f_names in os.walk(path):
        if d_names:
            for d_name in d_names:
                os.mkdir(root.replace("data_wage", "upgrate_data_wage") + "/" + d_name)
        if f_names:
            for f_name in f_names:
                #вставить функцию
                shutil.copy(root + "/" + f_name, root.replace("data_wage", "upgrate_data_wage") + "/" + f_name)
