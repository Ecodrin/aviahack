import os
import shutil


def main():
    path = './data_wage'
    os.mkdir("update_data_wage")
    for root, d_names, f_names in os.walk(path):
        if d_names:
            for d_name in d_names:
                os.mkdir(f"./update_{root[2:]}/{d_name}")
        if f_names:
            for f_name in f_names:
                #подставить функцию
                new_file = shutil.move(f"{root}/{f_name}", f"./update_{root[2:]}/{f_name}")


if __name__ == '__main__':
    main()
