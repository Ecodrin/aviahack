import shutil
import os
from file_enumerate import enumerate
from file_downenumerate import downenumerate
from data_loader import loader


def main():
    loader()
    #os.rename("data_wage", "data")
    os.rename("data_step", "data")
    #os.rename("data_car", "data")
    #os.rename("agard", "data")
    shutil.move("data", "../data")
    enumerate()
    downenumerate()


if __name__ == '__main__':
    main()
